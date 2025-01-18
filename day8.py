dog = {}

dog ['name'] = 'Buddy'
dog ['color'] = 'Brown' 
dog ['breed'] = 'Labrador'
dog ['legs'] = 4
dog ['age'] = 5

student = {
    'first_name': 'John',
    'last_name' : 'Doe',
    'gender'  : 'Male',
    'age' : 22,
    'marital status' : 'Single',
    'skills' : ['Python','Data Analysis']
}

#
length_of_student_dict = len(student)

skills_value = student['skills']
skills_type = type(skills_value)

student['skills'].extend(['Aws','Azure'])
print(student)