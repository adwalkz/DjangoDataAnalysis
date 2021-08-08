from django.shortcuts import render
from django.views import generic
from .models import Clients

class indexView(generic.ListView):
    """
    Handle index page request.
    """

    template_name = 'ts/index.html'
    context_object_name = 'latest_survey_list'

    def get_queryset(self):
        return Clients.objects.all()



