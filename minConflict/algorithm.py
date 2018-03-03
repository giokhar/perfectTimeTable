# from data import data, pretty_data
from minConflict.helper import *

def isAvailableAt(nextCourse, nextHour, nextDay):
	return not (nextDay, nextHour) in nextCourse.getNotAvailableAtList()

def isRecommendedAt(nextCourse, nextHour, nextDay, iterationN):
	notRecList = nextCourse.getNotRecommendedAtList()
	size = len(notRecList)
	index = iterationN * (size - 1) // 4
	return not (nextDay, nextHour) in notRecList[index:]

def isDoneSchedulling(course):
	return len(course.getSchedule()) == course.getFrequency()

def addDateToCourseSchedulle(nextCourse, nextDay, nextHour, conflictDict):
	nextCourse.addNewDateInSchedule((nextDay, nextHour))
	#______Fills in notAvailableAtList for the courses that are taught by same proffessor.
	sameProffCourses = conflictDict[nextCourse.getProffessor()] 
	for next in sameProffCourses:
		next.addNotAvailableTime((nextDay, nextHour))
	#_______Fills in notRecommendedAt list for the courses that have time conflicts in terms of students.
	stTimeConflictDict = nextCourse.getTimeConflictDict()
	for course, weight in stTimeConflictDict:
		course.addNotRecommendedTime((weight, (nextDay, nextHour)))

def chooseHour(nextCourse, nextDay, iterationN, conflictDict):
	for nextHour in range(8,9):
		if isAvailableAt(nextCourse, nextHour, nextDay) and isRecommendedAt(nextCourse, nextHour, nextHour, iterationN):
			addDateToCourseSchedulle(nextCourse, nextDay, nextHour, conflictDict)
			return

 
def scheduleNextCourse(nextCourse, nextDaysTuple, iterationN, conflictDict):
	for nextDay in nextDaysTuple:
		chooseHour(nextCourse, nextDay, iterationN, conflictDict)
		if isDoneSchedulling(nextCourse):
			return True

	if not isDoneSchedulling(nextCourse): 
		return False

def scheduller(coursesPriorityQueue, conflictDict):
	possWeekList = [('M', 'T', 'W', 'F'), ('M', 'W', 'F'),('M', 'R'), ('T', 'R'), ('T', 'F'), ('W', 'R'), ('W'), ('R')]

	while len(coursesPriorityQueue) != 0:
		nextCourse = heappop(coursesPriorityQueue)[1]
		done = False
		iterationN = 0

		while not done:
			if iterationN > 4:
				print("ERROR: Couldn't create schedule for", nextCourse.getTitle())
				break

			for nextDaysTuple in possWeekList:
				nextCourse.resetSchedule()

				if nextCourse.getFrequency() == len(nextDaysTuple):
					done = scheduleNextCourse(nextCourse, nextDaysTuple, iterationN, conflictDict)
					if done: break

			iterationN += 1


# if __name__ == '__main__':

# 	S1 = Student("ID", "student_id", "davite", "kvartskhava", 1, "computer science", [C1, C2, C3])
# 	S2 = Student("ID", "student_id", "davita", "kvartskhava", 1, "computer science", [C1, C2, C4])
# 	S3 = Student("ID", "student_id", "daviti", "kvartskhava", 1, "computer science", [C4, C3, C2])
# 	S4 = Student("ID", "student_id", "davito", "kvartskhava", 1, "computer science", [C4, C1, C5])
# 	S5 = Student("ID", "student_id", "davito", "kvartskhava", 1, "computer science", [C4, C1, C5])
# 	S6 = Student("ID", "student_id", "davito", "kvartskhava", 1, "computer science", [C4, C1, C5])
# 	S7 = Student("ID", "student_id", "davito", "kvartskhava", 1, "computer science", [C6, C2, C3])
# 	S8 = Student("ID", "student_id", "davito", "kvartskhava", 1, "computer science", [C4, C7, C6])
# 	S9 = Student("ID", "student_id", "davito", "kvartskhava", 1, "computer science", [C9, C8, C5])
# 	S10 = Student("ID", "student_id", "davito", "kvartskhava", 1, "computer science", [C9, C8, C5])

# 	lstStudents = []
# 	lstStudents.append(S1)
# 	lstStudents.append(S2)
# 	lstStudents.append(S3)
# 	lstStudents.append(S4)
# 	lstStudents.append(S5)
# 	lstStudents.append(S6)
# 	lstStudents.append(S7)
# 	lstStudents.append(S8)
# 	lstStudents.append(S9)
# 	lstStudents.append(S10)
	

# 	q = createCoursesPriorityQueue(lstCourses, lstStudents)
# 	scheduller(q)
# 	for nextCourse in lstCourses:
# 		print(nextCourse.getTitle(), "---" , nextCourse.getSchedule())