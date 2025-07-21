from .views import *
from django.urls import path
from .views import subject_list, test, subject_edit
from . import views

app_name = "planner"

urlpatterns = [
    path('index/', view=subject_list, name='subject_list'),
    path('test/', test),
    path('subjects/<int:subjecs_id>/edit/', subject_edit, name='subject_edit'),
    path('delete/<int:pk>/', views.delete_subject, name='delete_subject'),
    path('subject/add/', views.subject_create, name='subject_add'),
]