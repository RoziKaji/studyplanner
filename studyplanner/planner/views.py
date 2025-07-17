from django.shortcuts import render
from planner.models import subject
from .forms import SubjectForm

def subject_list(request):
    subjects = subject.objects.all()
    return render(request, 'index.html', {'subjects': subjects})

def add_subject(request):
    #if request.mode = 
    pass

def index(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")