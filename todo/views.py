from django.http import HttpResponse
from django.shortcuts import render,redirect ,get_object_or_404
from .models import Task

# Create your views here.
def addTask(req):
    task=req.POST['task']
    Task.objects.create(task=task )
    return redirect('home')
def mark_as_done(req, pk):
    task=get_object_or_404(Task, pk=pk)
    task.is_completed=True
    task.save()

    return redirect('home')

def mark_as_undone(req, pk):
    task=get_object_or_404(Task, pk=pk)
    task.is_completed=False
    task.save()

    return redirect('home')

def edit_task(req,pk):
    task = get_object_or_404(Task, pk=pk)
    if(req.method=='POST'):
        task.task=req.POST['task_new']
        task.save()
        return  redirect('home')
    else:
        context={
            'task':task
        }
        return render(req,'edit_task.html',context)

def delete_task(req, pk):
    task=get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

