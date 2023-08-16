from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import WorkerCreationForm
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


class PositionCreateView(generic.CreateView):
    model = Position
    fields = "__all__"
    template_name = "manager/position_form.html"
    success_url = reverse_lazy("manager:position-list")


class PositionUpdateView(generic.UpdateView):
    model = Position
    fields = "__all__"
    template_name = "manager/position_form.html"
    success_url = reverse_lazy("manager:position-list")


class TaskListView(generic.ListView):
    model = Task
    template_name = "manager/task_list.html"
    paginate_by = 5


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "manager/task_form.html"
    success_url = reverse_lazy("manager:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    template_name = "manager/task_form.html"
    success_url = reverse_lazy("manager:task-list")


class TaskTypeView(generic.ListView):
    model = TaskType
    template_name = "manager/task_type_list.html"
    paginate_by = 10


class TaskTypeCreateView(generic.CreateView):
    model = TaskType
    fields = "__all__"
    template_name = "manager/task_type_form.html"
    success_url = reverse_lazy("manager:task-type-list")


class TaskTypeUpdateView(generic.UpdateView):
    model = TaskType
    fields = "__all__"
    template_name = "manager/task_type_form.html"
    success_url = reverse_lazy("manager:task-type-list")


class WorkerView(generic.ListView):
    model = Worker
    template_name = "manager/worker_list.html"


class WorkerDetailView(generic.DetailView):
    model = Worker


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = "manager/worker_form.html"
