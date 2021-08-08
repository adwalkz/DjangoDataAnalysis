from django.urls import path
from . import views

app_name = "client"
urlpatterns = [
        path('<int:pk>/', views.index, name='index'), 
        path('<int:pk>/survey/', views.survey, name='survey'),
        path('<int:pk>/save/', views.save, name='save'),
        path('<int:pk>/feedback/', views.feedback, name='feedback')
]

