from django.shortcuts import render

# Create your views here.
def help_options(request):
	context={}
	return render(request,'help.html',context)