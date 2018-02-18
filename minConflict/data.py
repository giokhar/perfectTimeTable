import json

data = {}
courses = {}
students = {}

courses["cs128"] = {
	'title' : 'Programming & Problem Solving', 
	'professor' : 'barbeda', 
	'duration' : 60, 
	'frequency': 3
}

courses["econ100"] = { 
	'title' : 'Intro to Economics', 
	'professor' : 'krishra', 
	'duration' : 90, 
	'frequency': 2 
}

courses["cs440"] = { 
	'title' : 'Programming Languages', 
	'professor' : 'charliep', 
	'duration' : 90, 
	'frequency': 2
}

courses["econ205"] = { 
	'title' : 'Mathematical Foundations for Economics', 
	'professor' : 'krishra', 
	'duration' : 90, 
	'frequency': 2
}

courses["cs365"] = { 
	'title' : 'Artificial Intelligence and Machine Learning', 
	'professor' : 'barbeda', 
	'duration' : 90, 
	'frequency': 2
}


students[0] = {
	'name': "Giorgi Kharshiladze",
	'year': 3,
	'courses': ['cs128', 'cs365', 'econ205'],
	'major': 'econ'
}

students[1] = {
	'name': "Davit Kvartskhava",
	'year': 1,
	'courses': ['cs128', 'cs440', 'cs365'],
	'major': 'cs'
}

data['courses'] = courses
data['students'] = students

pretty_data = json.dumps(data, indent=4, sort_keys=True)
