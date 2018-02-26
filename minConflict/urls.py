from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from minConflict import views

urlpatterns = [
	url(r'^result/$', views.api, name='result'),
	url(r'^courses/$', views.CourseList.as_view(), name='course_api'),
	url(r'^courses/(?P<pk>[0-9]+)/$', views.CourseDetail.as_view(), name='course_detail_api'),
	url(r'^students/$', views.StudentList.as_view(), name='student_api'),
	url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view(), name='student_detail_api'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

