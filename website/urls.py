from django.conf.urls import url
from website import views

urlpatterns = [
	url(r'^$', views.index, name = "index"),
	url(r'^dashboard/$', views.dashboard, name='dashboard'),
	url(r'^login/$', views.login, name='login')
]