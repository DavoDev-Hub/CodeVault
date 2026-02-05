from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Task

def todo(request):
    todo_list = Task.objects.all()
    data = {'tasks': todo_list}
    return render(request, 'todo/todo.html', data)