from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from planner.models import subject, studysession
from .forms import SubjectForm
from django.urls import reverse
from django.http import JsonResponse
from datetime import datetime
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.dateparse import parse_datetime

def subject_list(request):
    subjects = subject.objects.all()
    return render(request, 'index.html', {'subjects': subjects})


def session_list(request):
    sessions = studysession.objects.select_related('subject').order_by('-start_session')
    subjects = subject.objects.all()
    return render(request, 'session.html', {'sessions': sessions, 'subjects': subjects})

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
        start = request.POST.get("start_session")
        end = request.POST.get("end_session")
        note = request.POST.get("note")

        subj = subject.objects.get(id=subject_id)
        studysession.objects.create(
            subject=subj,
            title=title,
            start_session=start,
            end_session=end,
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
    if request.method == "POST":
        session_id = request.POST.get("id")
        session = get_object_or_404(studysession, id=session_id)

        # سپس فیلدها رو آپدیت کن
        session.title = request.POST.get("title")
        session.start_session = request.POST.get("start_session")
        session.end_session = request.POST.get("end_session")
        session.note = request.POST.get("note")
        
        # subject
        subject_id = request.POST.get("subject")
        session.subject_id = subject_id
        
        session.save()

        return redirect("planner:index")  # یا هر صفحه‌ای که می‌خوای بعدش بره


def events_api(request):
    sessions = studysession.objects.all()
    
    events = []
    for s in sessions:

        events.append({
            "id": s.id,
            "title": f"{s.title} ({s.subject.name})",
            "start": s.start_session.isoformat(),
            "end": s.end_session.isoformat(),
            "backgroundColor": s.subject.color,
            "borderColor": s.subject.color,
            "textColor": "#000000",
            "allDay": False,
            "extendedProps": {
                "note": s.note or "",
                "subject": s.subject.name,
                "subject_id": s.subject.id,
            }
        })
    return JsonResponse(events, safe=False)


@csrf_exempt
def update_session_date(request):
    if request.method == "POST":
        data = json.loads(request.body)
        session_id = data.get("id")
        start = parse_datetime(data.get("start"))
        end = parse_datetime(data.get("end"))
    if start and timezone.is_aware(start):
        start = timezone.make_naive(start)

    if end and timezone.is_aware(end):
        end = timezone.make_naive(end)
        try:
            session = studysession.objects.get(id=session_id)
            session.start_session = start
            session.end_session = end if end else start
            session.save()
            return JsonResponse({"status": "ok"})
        except studysession.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

    return JsonResponse({"error": "Invalid method"}, status=400)


def test(request):
    return render(request, "test.html")