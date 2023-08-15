from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE,
                                 related_name="positions", blank=True,
                                 null=True)

    class Meta:
        ordering = ["username"]


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    CHOICES_FOR_PRIORITY = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("MustFix", "Must Fix"),

    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=50, choices=CHOICES_FOR_PRIORITY)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name="assignees")

    class Meta:
        ordering = ["deadline"]

    def __str__(self):
        return f"{self.name}\n{self.description}\n{self.deadline}"
