from django.db import connection
from random import randrange
import json

class Dashboard(object):

	def __init__(self, user):

		self.user = user
		self.email = user.email
		self.status = user.is_staff
	
	def isAdmin(self):
		return self.status

	def getEmail(self):
		return self.email


	# This is a recent semester for SQL query, getSemester is beautifier for that
	def getRecentSemester(self):
		cursor 	= connection.cursor()
		cursor.execute("SELECT recent.semester FROM (SELECT semester FROM students WHERE email=%s ORDER BY created_at DESC LIMIT 1) as recent;", [self.email])
		item = cursor.fetchone()[0]

		return item

	def getStudent(self):
		cursor 	= connection.cursor()
		cursor.execute("SELECT * FROM students WHERE email=%s AND semester=%s", [self.email, self.getRecentSemester()])
		desc = cursor.description
		return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()][0]

	def getFirstName(self):
		firstname = self.getStudent()['firstname'] or "n/a"
		return firstname

	def getLastName(self):
		lastname = self.getStudent()['lastname'] or "n/a"
		return lastname

	def getClassYear(self):
		class_year = self.getStudent()['class_year'] or "n/a"
		years = ["", "Freshman", "Sophomore", "Junior", "Senior"]
		ans = class_year
		if ans != "n/a":
			ans = years[ans]
		return ans

	def getClassYearNum(self):
		"""
		Class year number for the edit form
		"""
		return self.getStudent()['class_year'] or 1

	def getClassYears(self):
		"""
		List Classyear Names in the edit form
		"""
		class_years = ["", "Freshman", "Sophomore", "Junior", "Senior"]
		class_dict = {}

		for i in [1,2,3,4]:
			class_dict[i] = class_years[i]

		return class_dict.items()

	def getMajor(self):
		major = self.getStudent()['major'] or "n/a"
		return major

	def getSemester(self):
		semester = self.getRecentSemester().replace(":", " ")
		return semester.upper()

	def getPreferredCourses(self):
		preferred_courses = self.getStudent()['preferred_courses'] or "n/a"
		if preferred_courses == "n/a":
			return []

		course_dict = {}
		course_list = preferred_courses.split(",")[:-1]
		colors = ['red', 'pink', 'purple', 'blue', 'indigo', 'lime', 'orange', 'brown', 'grey', 'grey darken-4']

		for course in course_list:
			course_dict[course] = self.getCourse(course)
		
		for i in range(len(course_list)):
			c = course_list[i]
			course_dict[c][c]["priority"] = i+1
			course_dict[c][c]["percent"] = (10-i)*10
			course_dict[c][c]["color"] = colors[i]

		return course_dict.items()

	def getCourse(self, course):
		course_dict = {}

		cursor 	= connection.cursor()
		cursor.execute("SELECT * FROM courses WHERE cnr=%s", [course])
		desc = cursor.description
		course_dict[course] = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()][0]
		return course_dict


	def getFinalCourses(self):
		preferred_courses = self.getStudent()['final_courses'] or "n/a"
		json_courses = json.loads(preferred_courses)['final_courses'][0]
		return json_courses

	def getBackground(self):
		return 'images/gallary/'+ str(randrange(1,33)) +'.png'