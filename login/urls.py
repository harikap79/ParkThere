from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
#	url('', views.index, name = 'index'),
	url('', auth_views.login, {'template_name': 'login/LoginUI.html'}, name='login'),


]