from django.urls import path

from manager.views import index, PositionListView, TaskListView, TaskTypeView, \
    WorkerView, TaskDetailView

urlpatterns = [
    path("", index, name="index"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasktypes/", TaskTypeView.as_view(), name="task-type-list"),
    path("workers/", WorkerView.as_view(), name="worker-list"),
]

app_name = "manager"
