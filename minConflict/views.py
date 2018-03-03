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

from urllib.request import urlopen
import json

def getData(request, typeOf):
	url 		= "http://" + request.get_host() + "/api/" + typeOf +"/?format=json"
	jsonurl 	= urlopen(url)
	data		= json.loads(jsonurl.read())
	return data


def api(request):

	studentData = getData(request, "students")
	coursesData = getData(request, "courses")

	studentLst = []
	coursesLst = []
		
	for course in coursesData:
		one_course = Course(course['cnr'], course['course_number'], course['title'], course['duration'], course['frequency'], course['professor'], course['level'], course['num_enrolled'])
		coursesLst.append(one_course)

	for student in studentData:

		pref_courses = []
		if student['preferred_courses'] != None:

			my_courses = student['preferred_courses'].split(",")[:-1]

			for course in my_courses:
				#one_course_data
				o_c_d = getData(request, "courses/"+course)
				print(o_c_d)
				one_course = Course(o_c_d['cnr'], o_c_d['course_number'], o_c_d['title'], o_c_d['duration'], o_c_d['frequency'], o_c_d['professor'], o_c_d['level'], o_c_d['num_enrolled'])

				pref_courses.append(one_course)

			oneStudent = Student(student['id'], student['firstname'], student['lastname'], student['class_year'], student['major'], pref_courses)

			studentLst.append(oneStudent)

	q = createCoursesPriorityQueue(coursesLst, studentLst)
	scheduller(q)

	for nextCourse in coursesLst:
		print(nextCourse.getTitle(), "---" , nextCourse.getSchedule())


	result = studentData
	return render(request, "index.html", {"result": result})

class MajorList(APIView):
	def get(self, request):
		majors = MajorModel.objects.all()
		serializer = MajorSerializer(majors, many = True)

		return Response(serializer.data)

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
			return CourseModel.objects.get(cnr=pk)
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