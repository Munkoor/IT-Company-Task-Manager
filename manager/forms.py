from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from manager.models import Worker, Task


class DateInput(forms.DateInput):
    input_type = "date"


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "position", "first_name", "last_name")


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple)

    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4}))

    deadline = forms.DateField(widget=DateInput)

    class Meta:
        model = Task
        fields = "__all__"
