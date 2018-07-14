from django.conf.urls import url 
from . import views


urlpatterns = [
    url(r'^Students/$', views.Students_view, name='Students_view'),
    url(r'^Alumnis/$', views.Alumnis_view, name='Alumnis_view'),
    url(r'^Professors/$', views.Professors_view, name='Professors_view'),
    url(r'^Employees/$', views.Employees_view, name='Employees_view'),
      
]
