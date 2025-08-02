from django.urls import path
from . import views

app_name = "planner"

urlpatterns = [
    path('index/', views.subject_list, name='index'),
    path('sessions/', views.session_list, name='sessions'),
    path('test/', views.test),
    path('subjects/edit/', views.subject_edit, name='subject_edit'),
    path('delete/', views.delete_subject, name='delete_subject'),
    path('subject/add/', views.subject_create, name='subject_add'),
    path('add/', views.add_studysession, name='add_studysession'),
    path('delete-session/', views.delete_session, name='delete_session'),
    path('edit-session/', views.edit_session, name='edit_session'),
    path('api/events/', views.events_api, name='events_api'),
    path("api/update-session-date/", views.update_session_date, name="update_session_date"),

]
