'''Modify your program from excercise 6.2 so each person can have more than
one favorite number. Then print each person's name along with their 
favorite numbers.'''

fav_numbers = {'Paul': [4, 6, 12],
			'Peter': [6, 89, 77],
			'Bertje': [99, 23, 34],
			'Sjaak': [66, 75, 12],
			'Henk': [67, 21, 33],} 


for name, numbers in fav_numbers.items():
	print(name + "'s favorite numbers are: ")
	for number in numbers:
		print(number)
