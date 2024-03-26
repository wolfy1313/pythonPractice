contacts = {
  'number': 4,
  'students': 
    [
      {'name': 'Sarah Holder', 'email': 'sarah@example.com'},
      {'name': 'Sarah Collingslsf', 'email': 'Collingslsf@example.com'},
      {'name': 'Sarah Boulderdash', 'email': 'Boulderdash@example.com'},
      {'name': 'Sarah Hladskjfsd', 'email': 'Hladskjfsd@example.com'}
    ]
}

print('Student Emails: ')

for student in contacts['students']:
  print(student['email'])