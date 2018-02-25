from django.conf.urls import url
from minConflict import views

urlpatterns = [
	url(r'^$', views.api, name='api'),
]