from student import Student
from course import Course
from heapq import heappush
#Is given set of Classes and Students
def createCoursesPriorityQueue(lstCourses, lstStudents):
	for nextStudent in lstStudents:
		weight = 10
		for nextCourse in nextStudent.getPrefferedCourses():
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