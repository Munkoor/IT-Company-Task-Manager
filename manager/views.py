from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import WorkerCreationForm, TaskForm
from manager.models import Position, Task, TaskType, Worker


class IndexView(generic.ListView):
    template_name = 'manager/index.html'
    context_object_name = 'context'

    def get_queryset(self):
        num_of_positions = Position.objects.count()
        num_of_tasks = Task.objects.count()
        num_of_task_types = TaskType.objects.count()
        num_of_workers = Worker.objects.count()

        return {
            "num_of_positions": num_of_positions,
            "num_of_tasks": num_of_tasks,
            "num_of_task_types": num_of_task_types,
            "num_of_workers": num_of_workers,
        }


class PositionListView(generic.ListView):
    model = Position
    template_name = "manager/position_list.html"
    paginate_by = 5


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


class PositionDeleteView(generic.DeleteView):
    model = Position
    template_name = "manager/position_confirm_delete.html"
    success_url = reverse_lazy("manager:position-list")


class TaskListView(generic.ListView):
    model = Task
    template_name = "manager/task_list.html"
    paginate_by = 3


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "manager/task_confirm_delete.html"
    success_url = reverse_lazy("manager:task-list")


class TaskUpdateWorkerView(generic.UpdateView):
    def post(self, request, *args, **kwargs):
        worker = request.user
        task = get_object_or_404(Task, pk=kwargs["pk"])

        if worker in task.assignees.all():
            task.assignees.remove(worker)
        else:
            task.assignees.add(worker)

        return redirect("manager:task-detail", pk=kwargs["pk"])


class TaskTypeListView(generic.ListView):
    model = TaskType
    template_name = "manager/task_type_list.html"
    paginate_by = 5


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


class TaskTypeDeleteView(generic.DeleteView):
    model = TaskType
    template_name = "manager/task_type_confirm_delete.html"
    success_url = reverse_lazy("manager:task-type-list")


class WorkerListView(generic.ListView):
    model = Worker
    template_name = "manager/worker_list.html"
    paginate_by = 5


class WorkerDetailView(generic.DetailView):
    model = Worker


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = "manager/worker_form.html"
    success_url = reverse_lazy("manager:worker-list")


class WorkerUpdateView(generic.UpdateView):
    model = Worker
    fields = ["username", "first_name", "last_name", "position"]
    template_name = "manager/worker_form.html"
    success_url = reverse_lazy("manager:worker-list")


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("manager:index")
