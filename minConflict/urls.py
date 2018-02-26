from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from minConflict import views

urlpatterns = [
	url(r'^courses/', views.CourseList.as_view(), name='api'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

