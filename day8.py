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


# Get user input
age = int(input("Enter your age: "))

# Check if the user is 18 or older
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_needed = 18 - age
    print(f"You need {years_needed} more years to learn to drive.")