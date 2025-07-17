from .views import *
from django.urls import path

app_name = "planner"

urlpatterns = [
    path('index/', view=subject_list, name='subject_list'),
    path('test/', test)
]