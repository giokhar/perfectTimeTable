from data import data, pretty_data
from helper import *
from course import Course 
from student import Student 

if __name__ == '__main__':
	
	C1 = Course("ID",1, "C1", 1, 3, "ajika chavana", 2, 3)
	C2 = Course("ID",1, "C2", 1, 3, "ajika chavana", 2, 3)
	C3 = Course("ID",1, "C3", 1, 3, "ajika chavana", 2, 3)
	C4 = Course("ID",1, "C4", 1, 3, "ajika chavana", 2, 3)
	lstCourses = []
	lstCourses.append(C1)
	lstCourses.append(C2)
	lstCourses.append(C3)
	lstCourses.append(C4)

	S1 = Student("ID", "davit", "kvartskhava", 1, "computer science", [C1, C2, C3])
	S2 = Student("ID", "davita", "kvartskhava", 1, "computer science", [C1, C2, C4])
	S3 = Student("ID", "daviti", "kvartskhava", 1, "computer science", [C4, C3, C2])
	S4 = Student("ID", "davito", "kvartskhava", 1, "computer science", [C4, C1, C3])

	lstStudents = []
	lstStudents.append(S1)
	lstStudents.append(S2)
	lstStudents.append(S3)
	lstStudents.append(S4)

	print(createCoursesPriorityQueue(lstCourses, lstStudents))