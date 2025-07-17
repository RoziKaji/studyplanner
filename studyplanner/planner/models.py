from django.db import models
from datetime import datetime

# Create your models here.

class subject(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=13, choices={
        "#FFADAD" : "Melon",
        "#FFD6A5" : "Sunset",
        "#FDFFB6" : "Cream",
        "#CAFFBF" : "Tea green",
        "#9BF6FF" : "Electric blue",
        "#A0C4FF" : "Jordy Blue",
        "#BDB2FF" : "Periwinkle",
        "#FFC6FF" : "Mauve",
    })

    def __str__(self):
        return self.name
    
class studysession(models.Model):
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.subject)
    

def duration(self):
    start = datetime.combine(self.date, self.start_time)
    end = datetime.combine(self.date, self.end_time)
    return (end - start).seconds // 60

