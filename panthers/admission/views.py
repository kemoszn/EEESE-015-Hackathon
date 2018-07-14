from django.shortcuts import render
from .models import Admission
from .forms import AdmissionForm
from django.http import HttpResponse

def AdmissionRequest(request):
	if request.method == 'POST':
		admission_form = AdmissionForm(data=request.POST)
		if admission_form.is_valid():
			new_admission = admission_form.save(commit=False)
			new_admission.save()
			return HttpResponse("<h3> Thank you! Your request is being processed and we will provide you with the the necessary documents ASAP. </h3>")
	else:
		admission_form = AdmissionForm()

		return render(request, 'admission.html', {'admission_form': admission_form})

