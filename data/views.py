from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all().order_by('last_name')
    return render(request, 'employee_list.html', {'employees' : employees})
