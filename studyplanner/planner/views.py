from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from planner.models import subject
from .forms import SubjectForm
from django.urls import reverse

def subject_list(request):
    subjects = subject.objects.all()
    return render(request, 'index.html', {'subjects': subjects})

def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SubjectForm()
    return render(request, 'subject_create_form.html', {'form': form})

def subject_edit(request, subjecs_id):
    item = get_object_or_404(subject, pk=subjecs_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponse('<script>location.reload()</script>')
    else:
        form = SubjectForm(instance=item)
    return render(request, 'edit_subject_form.html', {'form': form, 'subject': item})

def delete_subject(request, pk):
    subj = get_object_or_404(subject, pk=pk)
    if request.method == 'POST':
        subj.delete()
        return redirect('subject_list') 
    return render(request, 'confirm_delete.html', {'subject': subj})
    

def test(request):
    return render(request, "test.html")