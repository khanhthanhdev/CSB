students = [{'firstName': 'Nikki', 'lastName': 'Roysden'},
{'firstName': 'Mervin', 'lastName': 'Friedland'},
{'firstName': 'Aron', 'lastName': 'Wilkins'}]

print('List of students: ')

for i in range(len(students)):
    for key in students[i]: 
        print(students[i][key],end=" "+'\n')