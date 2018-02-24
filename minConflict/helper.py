from student import Student
from course import Course
import heapq as PriorityQueue
#Is given list of Classes and Students
def createCoursesPriorityQueue(lstCourses, lstStudents):
	for nextStudent in lstStudents:
		weight = 10
		for nextCourse in nextStudent.getPrefferedCourses():
			nextCourse.incrementImportanceIndex(weight)
			weight -= 1

	for nextCourse in lstCourses:
		
