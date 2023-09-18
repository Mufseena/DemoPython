

from django import forms
from .models import Task


class Todo_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','priority','date']