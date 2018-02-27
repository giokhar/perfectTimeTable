# from data import data, pretty_data
from helper import *

# Import DB
# from django.db import connection

from urllib.request import urlopen
import json

# def scheduller(coursesPriorityQueue):
# 	possWeekList = [('M', 'W', 'F'), ('T', "R")]

# 	while len(coursesPriorityQueue) != 0:
# 		nextCourse = heappop(coursesPriorityQueue)

# 		for nextDaysTuple in possWeekList:
# 			if nextCourse.getFrequency() == len(nextDaysTuple):

# 				for nextDay in nextDaysTuple:
# 					for nextHour in range(8,11):
# 						if isAvailableAt(nextCourse, nextHour, nextDay):


def my_custom_sql():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    row = cursor.fetchone()
    return row

def getData(request, slug):
	host 		= "http://" + request.get_host() + "/"
	my_format 	= "/?format=json"
	url 		= host + slug + my_format

	jsonurl = urlopen(url)
	data = json.loads(jsonurl.read())

	return data


if __name__ == '__main__':
	
	C1 = Course("ID", 11, "C1", 1, 3, "ajika chavana", 2, 3)
	C2 = Course("ID", 12, "C2", 1, 3, "ajika chavana", 2, 3)
	C3 = Course("ID", 13, "C3", 1, 3, "giorga mavani", 2, 3)
	C4 = Course("ID", 14, "C4", 1, 3, "giorga mavani", 2, 3)
	C5 = Course("ID", 15, "C5", 1, 3, "ajit qvartskhava", 2, 3)

	lstCourses = []
	lstCourses.append(C1)
	lstCourses.append(C2)
	lstCourses.append(C3)
	lstCourses.append(C4)
	lstCourses.append(C5)

	S1 = Student("ID", "student_id", "davite", "kvartskhava", 1, "computer science", [C1, C2, C3])
	S2 = Student("ID", "student_id", "davita", "kvartskhava", 1, "computer science", [C1, C2, C4])
	S3 = Student("ID", "student_id", "daviti", "kvartskhava", 1, "computer science", [C4, C3, C2])
	S4 = Student("ID", "student_id", "davito", "kvartskhava", 1, "computer science", [C4, C1, C5])

	lstStudents = []
	lstStudents.append(S1)
	lstStudents.append(S2)
	lstStudents.append(S3)
	lstStudents.append(S4)

	print(createCoursesConflictDict(lstCourses))






