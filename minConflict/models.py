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
	student_id 			= models.IntegerField(unique = True, blank = True)
	firstname	 		= models.CharField(max_length = 255, blank = True)
	lastname 			= models.CharField(max_length = 255, blank = True)
	year	 			= models.IntegerField(blank = True)
	major	 			= models.CharField(max_length = 100, blank = True)
	preferred_courses 	= models.TextField(blank = True)
	final_courses 		= models.TextField(blank = True)


	def __str__(self): # Value that we see in DJANGO ADMIN
		return self.firstname + " " + self.lastname + " (student_id: " + str(self.student_id) + ")"

	class Meta:
		db_table = "students" # Table name in DB