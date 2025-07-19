from .views import *
from django.urls import path
from .views import subject_list, test, subject_edit

app_name = "planner"

urlpatterns = [
    path('index/', view=subject_list, name='subject_list'),
    path('test/', test),
    path('subjects/<int:subjecs_id>/edit/', subject_edit, name='subject_edit'),

]