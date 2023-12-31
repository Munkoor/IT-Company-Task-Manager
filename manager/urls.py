from django.urls import path

from manager.views import (
    IndexView,
    PositionListView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskUpdateWorkerView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/create/", PositionCreateView.as_view(),
         name="position-create"),
    path("positions/<int:pk>/update/", PositionUpdateView.as_view(),
         name="position-update"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(),
         name="position-delete"),

    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(),
         name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(),
         name="task-delete"),
    path("tasktypes/", TaskTypeListView.as_view(), name="task-type-list"),
    path("tasktypes/create/", TaskTypeCreateView.as_view(),
         name="task-type-create"),
    path("tasktypes/<int:pk>/update/", TaskTypeUpdateView.as_view(),
         name="task-type-update"),
    path("tasktypes/<int:pk>/delete/", TaskTypeDeleteView.as_view(),
         name="task-type-delete"),

    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(),
         name="worker-detail"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(),
         name="worker-update"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(),
         name="worker-delete"),
    path("workers/<int:pk>/update-worker/", TaskUpdateWorkerView.as_view(),
         name="task-update-worker")

]

app_name = "manager"
