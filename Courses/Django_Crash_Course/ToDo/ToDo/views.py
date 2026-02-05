from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from .models import Task

def task(request):
    task_list = Task.objects.all()
    data = {'Task': Task}
    return render(request, 'task/tasks.html', data)