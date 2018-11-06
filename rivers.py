'''Make a dictionary containing three major rivers and the country
each river runs through.'''

rivers  = {'Mississippi': 'USA',
			'Taag': "Spain",
			'Danube': 'Rumania',
			'Rijn': 'Nederland',
			'Seine': 'France',} 
			
'''Use a for loop to print a sentence about each river, such as
"The Nile runs through Egypt."'''

for key, value in rivers.items():
	print("The " + key + " runs through " + value + ".")

'''Use a loop to print the name of each country included in the dictionary.'''

for key in rivers.keys():
	print(key)

'''Use a loop to print the name of each country included in the dictionary'''

for value in rivers.values():
	print(value)
