from django.conf.urls import url
from website import views

urlpatterns = [
	url(r'^$', views.admin, name='index'),
	url(r'^login/$', views.login, name='login')
]