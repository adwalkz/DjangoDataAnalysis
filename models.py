from django.db import models
from ts.models import Clients

class SurveyQuestion(models.Model):
    QTYPES = ((1, 'TEXT'), (2, 'CHOICE'))

    company_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    ques_id = models.AutoField(primary_key=True) 
    ques_category = models.CharField(default="GENERAL", max_length=255)
    ques_type = models.IntegerField(default=1, choices=QTYPES)
    ques_text = models.CharField(max_length=255)
    ques_meta_1 = models.CharField(max_length=255)
    ques_meta_2 = models.CharField(max_length=255)

    def __str__(self):
        return self.company_id.client_name + ": " + self.ques_text
        #return self.ques_text


class SurveyQuestionChoice(models.Model):
    company_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    ques_id = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)

    def __str__(self):
        return "(" + self.ques_id.ques_text + ") " + self.choice_text


class SurveyResponse(models.Model):
    company_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    ques_id = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    user_response = models.CharField(max_length=255)

    def __str__(self):
        return self.user_response



