from .models import Admission
from django import forms

class AdmissionForm(forms.ModelForm):
	class Meta:
		model = Admission
		fields = ('name', 'email', 'index', 'Request')