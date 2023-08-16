from django.urls import path

from manager.views import index, PositionListView, TaskListView, TaskTypeView, \
    WorkerView, TaskDetailView, WorkerDetailView, PositionCreateView, \
    PositionUpdateView, TaskCreateView, TaskUpdateView, WorkerCreateView

urlpatterns = [
    path("", index, name="index"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/create/", PositionCreateView.as_view(),
         name="position-create"),
    path("positions/<int:pk>/update/", PositionUpdateView.as_view(),
         name="position-update"),

    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(),
         name="task-update"),
    path("tasktypes/", TaskTypeView.as_view(), name="task-type-list"),
    path("workers/", WorkerView.as_view(), name="worker-list"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(),
         name="worker-detail"),
]

app_name = "manager"
