from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from planner.models import subject, studysession
from .forms import SubjectForm,SessionForm
from django.urls import reverse


def subject_list(request):
    subjects = subject.objects.all()
    sessions = studysession.objects.select_related('subject').order_by('-date')
    return render(request, 'index.html', {'subjects': subjects, 'sessions': sessions})

def subject_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        color = request.POST.get("color")
        if name and color:
            subject.objects.create(name=name, color=color)
    return HttpResponseRedirect(reverse('planner:index'))


def subject_edit(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        item = get_object_or_404(subject, id=subject_id)
        form = SubjectForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponse('<script>location.reload()</script>')
    return redirect('planner:index')


def delete_subject(request):
    if request.method == 'POST':
        subject_id = request.POST.get("subject_id")
        subj = subject.objects.get(id=subject_id)
        subj.delete()
    return HttpResponseRedirect(reverse('planner:index'))
    

def add_studysession(request):
    if request.method == "POST":
        subject_id = request.POST.get("subject")
        title = request.POST.get("title")
        date = request.POST.get("date")
        start = request.POST.get("start_time")
        end = request.POST.get("end_time")
        note = request.POST.get("note")

        subj = subject.objects.get(id=subject_id)
        studysession.objects.create(
            subject=subj,
            title=title,
            date=date,
            start_time=start,
            end_time=end,
            note=note
        )
    return HttpResponseRedirect(reverse('planner:index'))

def delete_session(request):
    if request.method == 'POST':
        session_id = request.POST.get("session_id")
        ses = studysession.objects.get(id=session_id)
        ses.delete()
    return HttpResponseRedirect(reverse('planner:index'))

def edit_session(request):
    # if request.method == 'POST':
    #     session_id = request.POST.get('session_id')
    #     item = get_object_or_404(studysession, id=session_id)
    #     form = SessionForm(request.POST, instance=item)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse('<script>location.reload()</script>')
    # return redirect('planner:index')

    if request.method == "POST":
        session_id = request.POST.get("id")
        session = get_object_or_404(studysession, id=session_id)

        # سپس فیلدها رو آپدیت کن
        session.title = request.POST.get("title")
        session.date = request.POST.get("date")
        session.start_time = request.POST.get("start_time")
        session.end_time = request.POST.get("end_time")
        session.note = request.POST.get("note")
        
        # subject
        subject_id = request.POST.get("subject")
        session.subject_id = subject_id
        
        session.save()

        return redirect("planner:subject_list")  # یا هر صفحه‌ای که می‌خوای بعدش بره

    return redirect("planner:subject_list")


def test(request):
    return render(request, "test.html")