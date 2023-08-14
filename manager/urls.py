from django.contrib import admin
from django.urls import path, include

from manager.views import IndexView

urlpatterns = [
    path("", IndexView.as_view, name="index"),
]

app_name = "manager"
