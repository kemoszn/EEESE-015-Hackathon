from django.shortcuts import render

# Create your views here.
def AboutInfo(request):
	#context={}
	return render(request,'about.html')

