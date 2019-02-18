from django import forms
from django.contrib.auth.models import User
from .models import Task


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(label='Username')

    class Meta:
        model = User
        fields = ('username', 'password')


class TaskForm(forms.ModelForm):
    priority = forms.IntegerField(max_value=10, min_value=1)

    class Meta:
        model = Task
        fields = ('title', 'task', 'user', 'priority', 'category', 'due_time')


