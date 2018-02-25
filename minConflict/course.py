'''
Description
'''
import math
from datetime import time

class Course():
	def __init__(self, ID, courseNumber, title, duration, frequency, proffessor, level, numEnrolled):
		
		self.id = ID
		self.courseNumber = courseNumber
		self.title = title
		self.duration = duration
		self.frequency = frequency
		self.proffessor = proffessor
		self.level = level #3 = 300 level course
		self.importanceIndex = 0 #geometric mean of weights given by students
		self.numEnrolled = numEnrolled #actual number of students enrolled
		self.notAvailableAt = []
		self.finalSchedule = []
		self.timeConflictDict = {}

	#Increases the weight associated with each key
	#key = courseNumber, value = weight(initially 0)
	def addNewConflict(self, nextCourseNumber, coeff = 1):
		try:
			self.timeConflictDict[nextCourseNumber] += coeff
		except:
			self.timeConflictDict[nextCourseNumber] = 1

	def getTimeConflictDict(self):
		return self.timeConflictDict

	#Returns course number
	def getCourseNumber(self):
		return self.courseNumber

	#Returns level of the course
	def getLevel(self):
		return self.level

	#Returns importance index
	def getImportanceIndex(self):
		return self.importanceIndex

	#Returns the title of the course
	def getTitle(self):
		return self.title

	#Formulae for importanceIndex: sum / sqrt(numEnrolled)
	def incrementImportanceIndex(self, weight):
		self.importanceIndex += weight / math.sqrt(self.numEnrolled)

	#Is given a list of the tuples>>
	#Example(lst = [('M', 08:00:00(time object))])
	def excludeFollowingTimes(self, listOfNotAvailable):
		self.notAvailableAt += listOfNotAvailable


