from django.shortcuts import render

# Create your views here.
def ChatRoom_view(request):
	context={}

	return render(request,'ChatRoom_view_index.html',context)