from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')
    

class EventsAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'place', 'date')


    
admin.site.register(Event, EventsAdmin)
admin.site.register(New, NewsAdmin)