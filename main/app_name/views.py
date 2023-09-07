from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .forms import *
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def profile(request):
    user = request.user
    context = {"user":user.username}
    return render(request, "profile.html", context)

def taskcreate(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form=TaskForm()
    return render(request, 'task_create.html', {'form':form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks':tasks})

def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST,request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
        return render(request, 'task_update.html', {'form':form})
    
def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
            task.delete()
            return redirect('task_list')
    return render(request, 'task_delete.html')   