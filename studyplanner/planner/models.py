from django.db import models
from django.utils import timezone
from recurrence.fields import RecurrenceField

# Create your models here.

class subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    color = models.CharField(max_length=13,verbose_name="Color", choices={
        "#FFADAD" : "Melon",
        "#FFD6A5" : "Sunset",
        "#FDFFB6" : "Cream",
        "#CAFFBF" : "Tea green",
        "#9BF6FF" : "Electric blue",
        "#A0C4FF" : "Jordy Blue",
        "#BDB2FF" : "Periwinkle",
        "#FF9EFF" : "Mauve",
    })

    def __str__(self):
        return self.name
    
class RecurringStudySession(models.Model):
    title = models.CharField(max_length=200)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    recurrence = RecurrenceField()
    
class studysession(models.Model):
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_session = models.DateTimeField(default=timezone.now)
    end_session = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True, null=True)
    recurring = models.ForeignKey(RecurringStudySession, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.subject)
    

    
