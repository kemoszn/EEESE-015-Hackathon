from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Create your views here.
def Students_view(request):
	return render(request,'Students_view.html',{})

def Alumnis_view(request):

	return render(request,'Alumnis_view.html',{})

def Professors_view(request):
	
	return render(request,'Professors_view.html',{})	

def Employees_view(request):
	return render(request,'Employees_view.html',{})

def logout_view(request):
    logout(request)
    return HttpResponse('i did it!!')

