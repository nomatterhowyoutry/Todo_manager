from django.shortcuts import render
from todo.forms import UserForm, TaskForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *


@login_required
def todo_list(request):

    if request.method == 'POST':
        data = request.POST.items()
        for key, value in data:
            if value == 'Delete':
                delete_query(model=  Task,
                             id   =  key)
                tasks, failed = form_list(request)
                return render(request, 'todo/list.html', {'tasks': tasks, 'failed': failed})
        if request.POST.get('order_by') == 'priority':
            tasks, failed = sort_list(request, 'priority')
            return render(request, 'todo/list.html', {'tasks': tasks, 'failed': failed})
        if request.POST.get('order_by') == 'due_time':
            tasks, failed = sort_list(request, 'due_time')
            return render(request, 'todo/list.html', {'tasks': tasks, 'failed': failed})
    else:
        tasks, failed = form_list(request)
        return render(request, 'todo/list.html', {'tasks': tasks, 'failed': failed})


def sort_list(request, key):
    if key == 'priority':
        tasks = Task.objects.filter(user_id=request.user.id, due_time__gte=timezone.now()).order_by('-priority')
        failed = Task.objects.filter(user_id=request.user.id, due_time__lt=timezone.now()).order_by('-priority')
        return tasks, failed
    if key == 'due_time':
        tasks = Task.objects.filter(user_id=request.user.id, due_time__gte=timezone.now()).order_by('due_time')
        failed = Task.objects.filter(user_id=request.user.id, due_time__lt=timezone.now()).order_by('due_time')
        return tasks, failed


def delete_query(model, id):
    query = model.objects.filter(id=id)
    query.delete()


def form_list(request):
    tasks = Task.objects.filter(user_id=request.user.id, due_time__gte=timezone.now()).order_by('-created')
    failed = Task.objects.filter(user_id=request.user.id, due_time__lt=timezone.now()).order_by('-created')
    return tasks, failed


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('tasks'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'todo/signup.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('signup'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
    else:
        user_form = UserForm()
    return render(request,'todo/registration.html',
                          {'user_form':user_form,
                           'registered':registered})


def adding(request):
    if request.method == 'POST':
        task_form = TaskForm(data=request.POST)
        if task_form.is_valid():
            title = task_form.cleaned_data['title']
            task = task_form.cleaned_data['task']
            user = task_form.cleaned_data['user']
            priority = task_form.cleaned_data['priority']
            category = task_form.cleaned_data['category']
            due_time = task_form.cleaned_data['due_time']
            Task.objects.create(
                title=title,
                task=task,
                user=user,
                priority=priority,
                category=category,
                due_time=due_time)
            return HttpResponseRedirect(reverse('tasks'))
    else:
        task_form = TaskForm()
        return render(request, 'todo/adding.html', {'task_form' : task_form})