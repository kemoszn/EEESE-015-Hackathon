from django.conf.urls import url 
from . import views


urlpatterns = [
    url(r'^$', views.ChatRoom_view, name='ChatRoom_view'),
      
]
