from django.contrib import admin
from planner.models import *
# Register your models here.

admin.site.register(subject)
admin.site.register(studysession)
admin.site.register(RecurringStudySession)
admin.site.register(SkippedOccurrence)