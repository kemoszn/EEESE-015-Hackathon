from django.shortcuts import render

# Create your views here.
def Students_view(request):
	return render(request,'Students_view.html',{})

def Alumnis_view(request):

	return render(request,'Alumnis_view.html',{})

def Professors_view(request):
	
	return render(request,'Professors_view.html',{})	

def Employees_view(request):
	return render(request,'Employees_view.html',{})

