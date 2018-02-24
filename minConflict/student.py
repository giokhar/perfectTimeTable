'''Author: Davit Kvartskhava
	Class Description: class Student
	prefferedCourses: list of Course objects. Each student arranges courses in order of preference.
	In the given list the course at the 0 index is the most important one.
	 '''
class Student():
	def __init__(self, ID, firstName, lastName, year, major, prefferedCourses):
		self.ID = ID
		self.firstName = firstName
		self.lastName = lastName
		self.year = year #anticipated graduation year
		self.major = major
		self.prefferedCourses = prefferedCourses

	def getPrefferedCourses(self):
		return self.prefferedCourses