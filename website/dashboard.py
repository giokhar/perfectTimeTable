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

	def getMajor(self):
		major = self.getStudent()['major'] or "n/a"
		return major

	def getSemester(self):
		semester = self.getRecentSemester().replace(":", " ")
		return semester.upper()

	def getPreferredCourses(self):
		preferred_courses = self.getStudent()['preferred_courses'] or "n/a"
		json_courses = json.loads(preferred_courses)['preferred_courses'][0]
		return json_courses

	def getFinalCourses(self):
		preferred_courses = self.getStudent()['final_courses'] or "n/a"
		json_courses = json.loads(preferred_courses)['final_courses'][0]
		return json_courses

	def getBackground(self):
		return 'images/gallary/'+ str(randrange(1,33)) +'.png'