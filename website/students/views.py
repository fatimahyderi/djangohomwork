from django.shortcuts import get_object_or_404,render

# Create your views here.
from django.utils import timezone
from django.http import HttpResponse
from .models import Students,Attendance

def index(request):
    student_list = Students.objects.all() 
    context = {'student_list': student_list}
    return render(request, 'index.html', context)

def detail(request, student_id):
    student_name = get_object_or_404(Students, pk=student_id)
    current_month = timezone.now().month
    attendance_list = Attendance.objects.filter(student_id=student_id,date__month=current_month) 
    context = {'student_name':student_name,'attendance_list': attendance_list}
    return render(request, 'detail.html', context)