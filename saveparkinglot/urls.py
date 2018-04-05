from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
#	url('', views.index, name = 'index'),
	url(r'^$', views.SaveParkingLotView, name = 'saveParkingLot'),
    url('saved/', views.SavedParkingLotView, name = 'savedParkingLot')
	

]
