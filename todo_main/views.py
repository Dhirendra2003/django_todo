# from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(req):
  # return HttpResponse('<h1>Home page</h1>')
  tasks=Task.objects.filter(is_completed=False).order_by('created_at')
  completed_tasks=Task.objects.filter(is_completed=True).order_by('updated_at')
  # print(tasks)
  context={
    'tasks': tasks,
    'completed_tasks':completed_tasks
  }
  return render(req ,'home.html',context)