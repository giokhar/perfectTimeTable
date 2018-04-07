# from data import data, pretty_data
from minConflict.helper import *
from urllib.request import urlopen
import json

START_TIME = 8
END_TIME = 10

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
	for nextHour in range(START_TIME, END_TIME):
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

def getData(request, typeOf):
	url 		= "http://" + request.get_host() + "/api/" + typeOf +"/?format=json"
	jsonurl 	= urlopen(url)
	data		= json.loads(jsonurl.read())
	return data

def driver(request):

	studentData = getData(request, "students")
	coursesData = getData(request, "courses")

	studentLst = []
	coursesLst = []
		
	for course in coursesData:
		one_course = Course(course['cnr'], course['course_number'], course['title'], course['duration'], course['frequency'], course['professor'], course['level'], course['num_enrolled'])
		coursesLst.append(one_course)

	for student in studentData:

		pref_courses = []
		if student['preferred_courses'] != None:

			my_courses = student['preferred_courses'].split(",")[:-1]

			for course in my_courses:
				
				for that_course in coursesLst:
					if that_course.getID() == int(course):
						pref_courses.append(that_course)

			oneStudent = Student(student['id'], student['firstname'], student['lastname'], student['class_year'], student['major'], pref_courses)

			studentLst.append(oneStudent)
	conflictDict = createCoursesConflictDict(coursesLst) 
	q = createCoursesPriorityQueue(coursesLst, studentLst)
	scheduller(q, conflictDict)

	return coursesLst