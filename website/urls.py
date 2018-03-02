from django.conf.urls import url
from website.views import *

urlpatterns = [
	url(r'^$', index_view, name = "index"),
	url(r'^login/$', login_view, name='login'),
	url(r'^logout/$', logout_view, name='logout'),
	url(r'^register/$', register_view, name='register'),
	url(r'^dashboard/$', dashboard_view, name='dashboard'),
	url(r'^dashboard/edit/$', dashboard_view, name='dashboard_edit'),
	url(r'^dashboard/update/', dashboard_update, name='dashboard_update'),
	url(r'^registration/$', course_registration_view, name='course_registration'),
]