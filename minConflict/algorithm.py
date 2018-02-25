from data import data, pretty_data
from helper import *
from heapq import heappop
from course import Course
from student import Student 

# def scheduller(coursesPriorityQueue):
# 	possWeekList = [('M', 'W', 'F'), ('T', "R")]

# 	while len(coursesPriorityQueue) != 0:
# 		nextCourse = heappop(coursesPriorityQueue)

# 		for nextDaysTuple in possWeekList:
# 			if nextCourse.getFrequency() == len(nextDaysTuple):
# 				for nextDay in nextDaysTuple:
# 					for nextHour in range(8,13):
# 						if isAvailableAt(nextCourse, nextHour, )

if __name__ == '__main__':
	
	C1 = Course("ID",11, "C1", 1, 3, "ajika chavana", 2, 3)
	C2 = Course("ID",12, "C2", 1, 3, "ajika chavana", 2, 3)
	C3 = Course("ID",13, "C3", 1, 3, "ajika chavana", 2, 3)
	C4 = Course("ID",14, "C4", 1, 3, "ajika chavana", 2, 3)
	C5 = Course("ID",15, "C5", 1, 3, "ajika chavana", 2, 3)

	lstCourses = []
	lstCourses.append(C1)
	lstCourses.append(C2)
	lstCourses.append(C3)
	lstCourses.append(C4)
	lstCourses.append(C5)

	S1 = Student("ID", "davite", "kvartskhava", 1, "computer science", [C1, C2, C3])
	S2 = Student("ID", "davita", "kvartskhava", 1, "computer science", [C1, C2, C4])
	S3 = Student("ID", "daviti", "kvartskhava", 1, "computer science", [C4, C3, C2])
	S4 = Student("ID", "davito", "kvartskhava", 1, "computer science", [C4, C1, C5])

	lstStudents = []
	lstStudents.append(S1)
	lstStudents.append(S2)
	lstStudents.append(S3)
	lstStudents.append(S4)

	createTimeConflictDicts(lstStudents)

	for nextCourse in lstCourses:
		print(nextCourse.title,"-time conflict dict:", nextCourse.getTimeConflictDict())
