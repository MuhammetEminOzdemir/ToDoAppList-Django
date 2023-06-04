from django.shortcuts import render, HttpResponse, redirect
from .forms import TaskForm
from .models import Task

# Create your views here.


def index(request):
    # return HttpResponse("Hello World!!")
    form = TaskForm()

    if request.method == "POST":
        # Get the posted form
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")

    tasks = Task.objects.all() # add this
    return render(request, "index.html", {"task_form": form, "tasks": tasks})

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "update_task.html", {"task_edit_form": form})

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("index")
