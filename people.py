'''Start with the program you wrote for excercise 6.1.
Make two new dictionaries representing different people, and store all
three dictionaries in a list called people. Loop through your list of people.
As you loop through the list, print everything you know about each person.'''

person_1 = {'first_name': 'Eric',
			'last_name': 'van Rees',
			'age': 38,
			'city': 'Granada',}

person_2 = {'first_name': 'Piet',
			'last_name': 'Mondriaan',
			'age': 144,
			'city': 'Den Haag',}
			
person_3 = {'first_name': 'Klaas',
			'last_name': 'Vaak',
			'age': 23,
			'city': 'Bergen aan Zee'}

people = [person_1, person_2, person_3]
for p in people:
	print("\nName: " + p['first_name'])
	print("Last Name: " + p['last_name'])
	print("Age: " + str(p['age']))
	print("City: " + p['city'])
