from django.db import models

class Course(models.Model):

	id 				= models.AutoField(max_length = 5, primary_key = True)
	crn 			= models.IntegerField(unique = True)
	course_number 	= models.CharField(max_length = 50)
	title 			= models.CharField(max_length = 255)
	duration 		= models.DecimalField(max_digits = 3, decimal_places = 2)
	frequency 		= models.IntegerField()
	professor 		= models.CharField(max_length = 255)
	level 			= models.IntegerField()
	num_enrolled 	= models.IntegerField(blank = True, default = 0)
	final_schedule 	= models.TextField(blank = True)


	def __str__(self): # Value that we see in DJANGO ADMIN
		return self.course_number + " - " + self.title + "(CRN: " + str(self.crn) + ") - " + self.professor  

	class Meta:
		db_table = "courses" # Table name in DB


class Student(models.Model):

	id 					= models.AutoField(max_length = 5, primary_key = True)
	email 				= models.CharField(max_length = 255)
	semester 			= models.CharField(max_length = 100)
	firstname	 		= models.CharField(max_length = 255, null=True, blank = True)
	lastname 			= models.CharField(max_length = 255, null=True, blank = True)
	year	 			= models.IntegerField(null=True, blank = True)
	major	 			= models.CharField(max_length = 100, null=True, blank = True)
	preferred_courses 	= models.TextField(null=True, blank = True)
	final_courses 		= models.TextField(null=True, blank = True)


	def __str__(self): # Value that we see in DJANGO ADMIN
		return "email: " + str(self.email) + ")"

	class Meta:
		db_table = "students" # Table name in DB