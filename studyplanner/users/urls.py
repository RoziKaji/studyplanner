from django.urls import path
from . import views

urlpatterns=[
    path('login/', view = views.log_in, name = "login"),
]