from student import Student
from course import Course
from heapq import heappush, heappop

#Is given set of Classes and Students
def createCoursesPriorityQueue(lstCourses, lstStudents):
	for nextStudent in lstStudents:
		weight = 10
		for nextCourse in nextStudent.getPreferredCourses():
			nextCourse.incrementImportanceIndex(weight)
			weight -= 1

	coursesPriorityQueue = []
	for nextCourse in lstCourses:
		#100 l = 1.25, 200 = 1.50, 300 = 1.75, 400 = 2
		levelImportanceIndex = 1 + nextCourse.getLevel()/4
		#I am putting the the courses in the priority queue by the finalIndex, 
		#but I am dividing 1 on the index, so that the most important one
		#can be returned from the priority queue as the first element.
		finalIndex = 1 / (nextCourse.getImportanceIndex() * levelImportanceIndex)

		heappush(coursesPriorityQueue, (finalIndex, nextCourse.title))

	return coursesPriorityQueue

#Creates a dictionary for each Course object where the key is
#the courseNumber and the value is the number of time conflicts with 
#the course associated with the key. 
def createTimeConflictDicts(lstStudents):
	for nextStudent in lstStudents:
		for nextCourse in nextStudent.getPreferredCourses():
			for otherCourse in nextStudent.getPreferredCourses():
				if nextCourse != otherCourse:
					nextCourse.addNewConflict(otherCourse.getCourseNumber())
#Returns a dictionary where the courses within the same value
#have the same proffessor.
#The only reason why this kind of time coflicts can happen 
#are if the same proffessor teaches two different courses.
def createCoursesConflictDict(lstCourses):
	#This is a temporary dictionary, that stores 
	#proffessor:list of unique N of the classes he/she teaches -- as a key value pair
	tempDict = {}

	for nextCourse in lstCourses:
		nextProff = nextCourse.getProffessor()
		try:
			#if there is something associated with this key.
			tempDict[nextProff].append(nextCourse.getCourseNumber())
		except:
			tempDict[nextProff] = [nextCourse.getCourseNumber()]
	return tempDict















