dog = {}

dog['name'] = 'bunty'

dog['color'] = 'black'

dog['breed'] = 'Bull dog'

dog['legs'] = 4

dog['age'] = 2

print(dog)

student = dict()

student['first_name'] = 'Narayana Reddy'

student['last_name'] = 'Vemireddy'

student['gender'] = 'Male'

student['age'] = 21

student['Marital_status'] = 'No'

student['skills'] = ['python']

student['country'] = 'India'

student['city'] = 'khammam'

student['address'] = 'main road Banjara'

print(student)

len_of_student = len(student)

print(len_of_student)

skills_of_student = student.get('skills')

print(skills_of_student)

print(type(skills_of_student))

student.update({'skills': ['C', 'Java', 'Pyspark', 'Angular']})

print(student)

student_keys = list(student.keys())

print(student_keys)

student_values = list(student.values())

print(student_values)

