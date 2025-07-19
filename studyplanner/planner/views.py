from django.shortcuts import render, get_object_or_404, redirect
from planner.models import subject
from .forms import SubjectForm
from django.urls import reverse

def subject_list(request):
    subjects = subject.objects.all()
    return render(request, 'index.html', {'subjects': subjects})

def add_subject(request):
    #if request.mode = 
    pass

def subject_edit(request, subjecs_id):
    item = get_object_or_404(subject, pk=subjecs_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('planner:subject_list')
    else:
        form = SubjectForm(instance=item)
    return render(request, 'edit_subject.html', {'form': form, 'subject': item})

def test(request):
    return render(request, "test.html")