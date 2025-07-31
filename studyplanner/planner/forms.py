from django import forms
from .models import subject,studysession

class SubjectForm(forms.ModelForm):
    class Meta:
        model = subject
        fields=['name', 'color']

class SessionForm(forms.ModelForm):
    class Meta:
        model = studysession
        fields=['subject', 'title', 'start_session', 'end_session', 'note']