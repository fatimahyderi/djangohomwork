from django.contrib import admin

# Register your models here.

from .models import Students,Attendance
admin.site.register(Students)
admin.site.register(Attendance)