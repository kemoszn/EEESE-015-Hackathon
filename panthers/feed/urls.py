from django.conf.urls import url 
from . import views


urlpatterns = [
    url(r'^News/$', views.news_list, name='news_list'),
     url(r'^Events/$', views.events_list, name='events_list'),
    
    
]
