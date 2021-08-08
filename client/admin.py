from django.contrib import admin
from .models import SurveyQuestion, SurveyQuestionChoice

admin.site.register(SurveyQuestion)
admin.site.register(SurveyQuestionChoice)

