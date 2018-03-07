from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from home.models import CarPark

urlpatterns = [
#	url('', views.index, name = 'index'),
	url(r'^(?P<id>[\d]+)/$', views.carParkInfo, name = "info"),


]