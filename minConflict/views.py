from django.shortcuts import render
from django.http import Http404, HttpResponse

# import rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# import my serializers & models
from minConflict.serializers import *
# import my algorithm
from minConflict.algorithm import *


def api(request):
	# result = getData(request, "api/students")
	result = retrieve()
	return HttpResponse(result)

class CourseList(APIView):
	"""
	List all the courses as a RESTapi
	"""
	def get(self, request):
		courses = CourseModel.objects.all() # CourseModel located in serializers
		serializer = CourseSerializer(courses, many = True)

		return Response(serializer.data)

class CourseDetail(APIView):
	"""
	Show details for each course as a RESTapi
	"""
	def get_object(self, pk):
		try:
			return CourseModel.objects.get(pk=pk)
		except CourseModel.DoesNotExist:
			raise Http404()

	def get(self, request, pk):
		course = self.get_object(pk)
		serializer = CourseSerializer(course)
		return Response(serializer.data)

class StudentList(APIView):
	"""
	List all the students as a RESTapi
	"""
	def get(self, request):
		students = StudentModel.objects.all() # CourseModel located in serializers
		serializer = StudentSerializer(students, many = True)

		return Response(serializer.data)

class StudentDetail(APIView):
	"""
	Show details for each student as a RESTapi
	"""
	def get_object(self, pk):
		try:
			return StudentModel.objects.get(pk=pk)
		except StudentModel.DoesNotExist:
			raise Http404()

	def get(self, request, pk):
		student = self.get_object(pk)
		serializer = StudentSerializer(student)
		return Response(serializer.data)