from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def addTask(req):
    task=req.POST['task']
    Task.objects.create(task=task )
    return redirect('home')