from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Task

def todo(request):
    todo_list = Task.objects.all()
    data = {'tasks': todo_list}
    return render(request, 'todo/todo.html', data)

def detail(request, id):
    data = Task.objects.get(id=id)
    return render(request, 'todo/detail.html', {'Task': data})

def add(request):
    task_title = request.POST.get('task_title')
    description = request.POST.get('description')

    if task_title and description:
        task = Task(task_title=task_title, description=description)
        task.save()
        return HttpResponseRedirect('/todo')
    return render(request, 'todo/add.html')