from django import forms
from .models import subject

class SubjectForm(forms.ModelForm):
    class Meta:
        model = subject
        fields=['name', 'color']