from django.conf.urls import url
from website.views import *

urlpatterns = [
	url(r'^$', index_view, name = "index"),
	url(r'^login/$', login_view, name='login'),
	url(r'^logout/$', logout_view, name='logout'),
	url(r'^register/$', register_view, name='register'),
	url(r'^dashboard/$', dashboard_view, name='dashboard'),
	url(r'^dashboard/edit/$', profile_edit_view, name='edit'),
]