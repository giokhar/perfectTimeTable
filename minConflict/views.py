from django.shortcuts import render, get_object_or_404

# import rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# import my models
from .models import Course as CourseModel, Student as StudentModel
from .serializers import CourseSerializer, StudentSerializer
# import my algorithm
from minConflict.algorithm import *


class CourseList(APIView):

	def get(self, request):
		courses = CourseModel.objects.all()
		serializer = CourseSerializer(courses, many = True)

		return Response(serializer.data)

	# def post(self):
	# 	pass
