from typing import ContextManager
from django.contrib.auth import authenticate, forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ImageForm

# # Create your views here.

def register(request):    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
        
    return render(request, 'register.html',{'form':form})

def login(request):
      return render(request, 'login.html') 
    
def dashboard(request):
     movies = Movie.objects.all()
     context = {'movies':movies}
     return render(request, 'dashboard.html',context)

def movies(request):
    if request.method == "POST":
        form = ImageForm(data = request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return redirect('/dashboard/') 
    else:
        form = ImageForm()
        img = Movie.objects.all()
    return render(request, 'movies.html',{'img':img,'form':form}) 
      
@login_required
def logout(request):
     return render(request, 'logout.html')