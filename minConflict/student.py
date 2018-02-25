'''
Description:
'''

class Student():
	def __init__(self, ID, studentId, firstName, lastName, year, major, preferredCourses):
		
		self.ID = ID,
		self.studentId = studentId
		self.firstName = firstName
		self.lastName = lastName
		self.year = year # class year
		self.major = major
		# #preferredCourses: list of Course objects. Each student arranges courses in order of preference.
		# In the given list the course at the 0 index is the most important one.
		self.preferredCourses = preferredCourses

	def getPreferredCourses(self):
		return self.preferredCourses