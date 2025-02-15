from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Task
from django.contrib import messages
from home.middleware import LoginReq
from home.forms import TaskForm
#from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():

            user=form.save()
            login(request,user)
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created!{username}')
            return redirect('login')
        else:
            return render(request, 'register.html', {'form':form})
    else:
        form=UserCreationForm()
        return render(request, 'register.html', {'form':form})

def login_view(request):
      if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Get the authenticated user
            login(request, user)
           
            return redirect('dashboard')
        else:
            #print(form.errors)
            return render(request, 'login.html', {'form': form})
      else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})




@LoginReq
def dashboard(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Create the task and associate it with the logged-in user
        task = Task(title=title, description=description, user=request.user)
        task.save()
        messages.success(request, "Task added successfully!")

        return redirect('dashboard')
    else:
        # Retrieve tasks belonging to the logged-in user
        tasks = Task.objects.filter(user=request.user)

        return render(request, 'dashboard.html', {'tasks': tasks,'username': request.user.username})



def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out!!.")
    return redirect('index')

def edit_task(request,task_id):
    
        task=get_object_or_404(Task,id=task_id)
        if request.method == 'POST':
            form = TaskForm(request.POST, instance=task)
            if form.is_valid:
                form.save()
                return redirect('dashboard')
            
        else:
            form = TaskForm(instance=task)
        return render(request, 'edit_task.html', {'form': form,'task':task})
        
def delete_task(request,task_id):
    task=get_object_or_404(Task,id=task_id)
    task.delete()
    return redirect('dashboard')
    
   
            




   
