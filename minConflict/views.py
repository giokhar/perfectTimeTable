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
import json

def api(request):

	url 		= "http://" + request.get_host() + "/api/students/?format=json"
	jsonurl 	= urlopen(url)
	data 		= json.loads(jsonurl.read())
		
	S1 = Student("ID", "student_id", "davite", "kvartskhava", 1, "computer science", [C1, C2, C3])
	S2 = Student("ID", "student_id", "davita", "kvartskhava", 1, "computer science", [C1, C2, C4])
	S3 = Student("ID", "student_id", "daviti", "kvartskhava", 1, "computer science", [C4, C3, C2])
	S4 = Student("ID", "student_id", "davito", "kvartskhava", 1, "computer science", [C4, C1, C5])
	S5 = Student("ID", "student_id", "davito", "kvartskhava", 1, "computer science", [C4, C1, C5])
	S6 = Student("ID", "student_id", "davito", "kvartskhava", 1, "computer science", [C4, C1, C5])
	S7 = Student("ID", "student_id", "davito", "kvartskhava", 1, "computer science", [C6, C2, C3])
	S8 = Student("ID", "student_id", "davito", "kvartskhava", 1, "computer science", [C4, C7, C6])
	S9 = Student("ID", "student_id", "davito", "kvartskhava", 1, "computer science", [C9, C8, C5])
	S10 = Student("ID", "student_id", "davito", "kvartskhava", 1, "computer science", [C9, C8, C5])

	lstStudents = []
	lstStudents.append(S1)
	lstStudents.append(S2)
	lstStudents.append(S3)
	lstStudents.append(S4)
	lstStudents.append(S5)
	lstStudents.append(S6)
	lstStudents.append(S7)
	lstStudents.append(S8)
	lstStudents.append(S9)
	lstStudents.append(S10)

	q = createCoursesPriorityQueue(lstCourses, lstStudents)
	scheduller(q)

	for nextCourse in lstCourses:
		print(nextCourse.getTitle(), "---" , nextCourse.getSchedule())


	result = data
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