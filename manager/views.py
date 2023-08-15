from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic

from manager.models import Position, Task, TaskType, Worker


@login_required
def index(request):
    """View function for the home page of the site."""

    num_of_positions = Position.objects.count()
    num_of_tasks = Task.objects.count()
    num_of_task_types = TaskType.objects.count()
    num_of_workers = Worker.objects.count()

    context = {
        "num_of_positions": num_of_positions,
        "num_of_tasks": num_of_tasks,
        "num_of_task_types": num_of_task_types,
        "num_of_workers": num_of_workers,
    }

    return render(request, "manager/index.html", context=context)
