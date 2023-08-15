from django.urls import path

from manager.views import index, PositionListView, TaskListView, TaskTypeView

urlpatterns = [
    path("", index, name="index"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasktypes/", TaskTypeView.as_view(), name="task-type-list")
]

app_name = "manager"
