from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
#	url('', views.index, name = 'index'),
	url(r'^$', views.saveParkingLot, name = 'saveParkingLot'),
        url('saved/', views.savedParkingLot, name = 'savedParkingLot')
	

]
