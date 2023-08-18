from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from manager.models import Position, TaskType, Task, Worker


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "deadline", "is_completed"]


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    search_fields = ["username", "first_name", "last_name", "position"]
    list_display = UserAdmin.list_display + ("position",)



