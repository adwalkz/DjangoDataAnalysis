from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Count, Avg, Max, Min

from ts.models import *
from .models import SurveyQuestion, SurveyQuestionChoice, SurveyResponse

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, client_name):
        super().__init__()
        self.WIDTH = 210
        self.HEIGHT = 297
        self.name = client_name

    def header(self):
        self.image('ts/static/ts/index.png', 10, 3, 33)
        self.set_font('Arial', 'B', 11)
        self.cell(self.WIDTH - 80)
        self.cell(60, 1, self.name.upper() + ' SURVEY REPORT', 0, 0, 'R')
        self.ln(20)

    def footer(self): 
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def page_body(self, images):
        self.image(images, 15, 35, self.WIDTH)

    def print_page(self, images): 
        self.add_page()
        self.page_body(images)


def index(request, pk):
    """
    This view is for
    creating dynamic
    and personalized
    client home page
    """

    ques_obj = SurveyQuestion.objects.filter(company_id=pk)
    res_obj = SurveyResponse.objects.filter(company_id=pk)

    total_survey_question = ques_obj.count()
    total_survey_response = res_obj.count()//total_survey_question

    stats_list = []
    charts = []
    for q in ques_obj:
        if q.ques_type == 1:
            res_obj = SurveyResponse.objects.filter(ques_id_id = q.ques_id)
            stat_dic =  res_obj.aggregate( \
                    Avg('user_response'), \
                    Max('user_response'), \
                    Min('user_response'))

            stat_dic['ques'] = q.ques_text
            stats_list.append(stat_dic)
        elif q.ques_type == 2: 
            choice_list = []
            res_list = []
            stats = []

            res_obj = SurveyResponse.objects.filter(ques_id_id = q.ques_id)
            choice_obj = SurveyQuestionChoice.objects.filter(ques_id_id = q.ques_id)

            choice_list = [c.choice_text for c in choice_obj]
            res_list = [r.user_response for r in res_obj]
            stats = [res_list.count(i) for i in set(res_list)]
            name = str(q.company_id_id) + '_' + str(q.ques_id)
 
            plt.pie(stats, labels=set(res_list), autopct='%1.0f%%')
            plt.title(q.ques_text)
            plt.legend()
            plt.savefig('client/static/client/charts/' + name + '.png', \
                    transparent=True)
            plt.close()
            charts.append(name)

    context = {
            'client': get_object_or_404(Clients, pk=pk),
            'total_ques': total_survey_question,  
            'total_response': total_survey_response, 
            'charts': charts,
            'stats': stats_list
    }

    pdf = PDF(context['client'].client_name)
    for i in charts:
        pdf.print_page('client/static/client/charts/' + i + '.png')

    pdf.output('client/static/client/' + str(pk) +'.pdf', 'F')

    return render(request, "client/index.html", context)


def survey(request, pk):
    """
    This view is for
    creating dynamic
    and personalized
    client survey page
    """

    context = {
            'client': get_object_or_404(Clients, pk=pk),
            'categories': SurveyQuestion.objects.filter(company_id=pk).values('ques_category').annotate(Count('ques_category')).order_by(),
            'ques_set': SurveyQuestion.objects.filter(company_id=pk),
            'choice_set': SurveyQuestionChoice.objects.filter(company_id=pk)
    } 

    return render(request, "client/survey.html", context)


def save(request, pk):
    """
    This view is for
    saving participant
    response into db
    """

    context = {
            'client': get_object_or_404(Clients, pk=pk)
    }

    for res in request.POST:
        if res == "csrfmiddlewaretoken" or res == "submit":
            continue

        response = SurveyResponse(
                company_id = Clients.objects.get(pk=pk), 
                ques_id = SurveyQuestion.objects.get(pk=int(res)), 
                user_response=request.POST[res]
        )

        response.save()

    return render(request, "client/thanks.html", context)


def feedback(request, pk):
    """
    This view is for
    saving participant
    feedback regarding
    survey
    """

    context = {'client': get_object_or_404(Clients, pk=pk)}
    return render(request, "client/feedback.html", context)

