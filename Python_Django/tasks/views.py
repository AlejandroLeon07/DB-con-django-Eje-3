from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import RegistrarCurso

# Create your views here.


def home(request):
    return render(request, 'Home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('task')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username alreasy exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'password do not match'
            })
        


def task(request):
    return render(request, 'task.html')

def create_register(request):
    if request.method =='GET':
        return render(request, 'create_register.html', {
        'form': RegistrarCurso
        })
    else:
        try:
            form = RegistrarCurso(request.POST)
            nueva_tarea = form.save(commit=False)
            nueva_tarea.user = request.user
            nueva_tarea.save()
            return redirect('task')
        except ValueError:
            return render(request, 'create_register.html',{
            'form': RegistrarCurso,
            'error': 'Por favor ingrese un valor valido'
        })
    
        
        
    

def signout(request):
    logout(request)
    return redirect('Home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
        'form': AuthenticationForm
    })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'signin.html',{
            'form': AuthenticationForm,
            'error': 'Username or password is incorrect'
        })
        else:
            login(request, user)
            return redirect('task')
        
