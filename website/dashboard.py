from django.db import connection

class Dashboard(object):

	def __init__(self, user):

		self.user = user
		self.email = user.email
		self.status = user.is_staff
	
	def isAdmin(self):
		return self.status	

	def getEmail(self):
		return self.email

	def getRecentSemester(self):
		cursor 	= connection.cursor()
		cursor.execute("SELECT recent.semester FROM (SELECT semester FROM students WHERE email=%s ORDER BY created_at DESC LIMIT 1) as recent;", [self.email])
		item = cursor.fetchone()[0]

		return item