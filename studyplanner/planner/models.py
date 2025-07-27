from django.db import models
from datetime import datetime

# Create your models here.

class subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    color = models.CharField(max_length=13,verbose_name="رنگ", choices={
        "#FFADAD" : "گلبهی",
        "#FFD6A5" : "هلویی",
        "#FDFFB6" : "نباتی",
        "#CAFFBF" : "نعنایی",
        "#9BF6FF" : "ابی برفی",
        "#A0C4FF" : "نیلی",
        "#BDB2FF" : "یاسی",
        "#FF9EFF" : "صورتی شفقی",
    })

    def __str__(self):
        return self.name
    
class studysession(models.Model):
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
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

