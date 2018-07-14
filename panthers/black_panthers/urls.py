from django.conf.urls import url 
from . import views
from django.contrib.auth.views import login, logout



urlpatterns = [
   url(r'^Students/login/$', login, name='login'),
    url(r'^Alumnis/login/$', login, name='Alumnis_viewlogin'),
    url(r'^Professors/login/$', login, name='Professors_viewlogin'),
    url(r'^Employees/login/$', login, name='Employees_viewlogin'),
    #log out
    url(r'^Students/logout/$', views.logout_view, name='Students_viewlogout_view'),
    url(r'^Alumnis/logout/$', views.logout_view, name='Alumnis_viewlogout_view'),
    url(r'^Professors/logout/$', views.logout_view, name='Professors_viewlogout_view'),
    url(r'^Employees/logout/$', views.logout_view, name='Employees_viewlogout_view'),
      
      
]
