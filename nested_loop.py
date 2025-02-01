contacts = {
    'number': 5,
    'students': [
        {'name': 'Kathiravan', 'email': 'kathir@example.com'},
        {'name': 'Karthickeyan', 'email': 'karthickeyan@example.com'},
        {'name': 'Aadhikesavan', 'email': 'aadhi@example.com'},
        {'name': 'Raja', 'email': 'raja@example.com'},
    ]
}

# Print all students email:
print("Student emails:")
for student in contacts.get('students'):
    print(student.get('email'))