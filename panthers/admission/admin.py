from django.contrib import admin
from .models import * 


class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'Request', 'publish','index')

admin.site.register(Admission, AdmissionAdmin)