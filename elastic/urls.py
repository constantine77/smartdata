from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^search/$', views.my_search),
]
