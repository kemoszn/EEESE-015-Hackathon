from django.conf.urls import url 
from . import views


urlpatterns = [
    url(r'^News/$', views.news_list, name='news'),
    url(r'^Events/$', views.events_list, name='events'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<news>[-\w]+)/$', views.news_detail, name='news_detail'),
    url(r'^Events/Add/$', views.AddEvent, name='AddEvent'),
    
]
