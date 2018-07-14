from django.conf.urls import url 
from . import views


urlpatterns = [
    url(r'^$', views.help_options, name='help_options'),
      
]
