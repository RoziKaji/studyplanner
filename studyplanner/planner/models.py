from django.db import models
from datetime import datetime
from django.utils import timezone

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
    
class studysession(models.Model):
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_session = models.DateTimeField(default=timezone.now)
    end_session = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.subject)
    
