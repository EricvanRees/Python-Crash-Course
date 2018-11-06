'''Make a dictionary called favorite_places. Think of three names to use
as keys in the dictionary, and store one to three favorite places for each
person. Loop through the dictionary and print each person's name and 
favorite places.'''

favorite_places = {'Eric': ['Paris', 'Granada', 'Salamanca'],
					'Regina': ['Constanta', 'Zwolle', 'Leiden'],
					'Tom': ['Enschede', 'Genemuiden', 'Tokyo'],}

for name, places in favorite_places.items():
	print(name + "'s favorite cities are: ")
	for place in places:
		print(place)
