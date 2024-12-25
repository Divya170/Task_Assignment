from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, TaskForm
from .models import Task, User
# Create your views here.
# users/views.py


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('task_dashboard')  # Redirect to dashboard on successful login
    else:
        form = AuthenticationForm()
    return render(request,'login.html', {'form': form})

# @login_required
# def task_dashboard(request):
#     tasks = Task.objects.filter(assigned_to=request.User)
#     return render(request,'task_dashboard.html', {'tasks': tasks})

@login_required
def task_dashboard(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'task_dashboard.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=True)
            task.save()
            # Send notification email
            # send_mail(
            #     'New Task Assigned',
            #     f'Task "{task.name}" has been assigned to you.',
            #     'your_email@example.com',
            #     [task.assigned_to.email],
            # )
            return redirect('task_dashboard')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request,'edit_task.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_dashboard')

def logout_view(request):
    logout(request)
    return redirect('login')

