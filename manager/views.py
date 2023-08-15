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


class PositionListView(generic.ListView):
    model = Position
    template_name = "manager/position_list.html"
    paginate_by = 10


class TaskListView(generic.ListView):
    model = Task
    template_name = "manager/task_list.html"
    paginate_by = 5


class TaskDetailView(generic.DetailView):
    model = Task


class TaskTypeView(generic.ListView):
    model = TaskType
    template_name = "manager/task_type_list.html"
    paginate_by = 10


class WorkerView(generic.ListView):
    model = Worker
    template_name = "manager/worker_list.html"

