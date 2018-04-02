from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
url('login/$', auth_views.login, {'template_name': 'login/LoginUI.html'}, name='login'),
	  url('^', include('django.contrib.auth.urls')),
      url('password_reset/$', auth_views.password_reset,name='password_reset'),
      url('password_reset/done/$', auth_views.password_reset_done,name='password_reset/done'),
      url('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm,name='reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})'),
      url('reset/done/', auth_views.password_reset_complete,name='reset/done'),



]