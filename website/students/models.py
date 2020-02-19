from django.db import models
from django.utils import timezone
# Create your models here.

class_attendance = (
    ('Present','Present'),
    ('Absent','Absent'),
)

class Students(models.Model):
    student_name = models.CharField(max_length=55)

    def __str__(self):
        return self.student_name

class Attendance(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now())
    mark_attendance = models.CharField(max_length=50, choices=class_attendance,default='not marked')

    def __str__(self):
        return self.mark_attendance

    