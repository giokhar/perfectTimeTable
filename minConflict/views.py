from django.shortcuts import render
from django.http import Http404

# import rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# import my serializers & models
from minConflict.serializers import *
# import my algorithm
from minConflict.algorithm import *


class CourseList(APIView):
	"""
	List all the courses using RESTapi
	"""
	def get(self, request):
		courses = CourseModel.objects.all() # CourseModel located in serializers
		serializer = CourseSerializer(courses, many = True)

		return Response(serializer.data)

class CourseDetail(APIView):
	"""
	Show details for each course in RESTapi
	"""
	def get_object(self, pk):
		try:
			return CourseModel.objects.get(pk=pk)
		except CourseModel.DoesNotExist:
			raise Http404()

	def get(self, request, pk):
		snippet = self.get_object(pk)
		serializer = CourseSerializer(snippet)
		return Response(serializer.data)
