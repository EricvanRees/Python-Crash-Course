'''Choose any three programs you wrote for this chapter, and make sure
they follow the styling guidelines described in this section'''

# program 1:
def make_sandwich(*ingredients):
	'''function takes multiple parameters ,
	creates a sandwich of all parameters, then prints all parameters'''
	print("Your sandwich has: ")
	for ingredient in ingredients:
		print("-" + ingredient)	

make_sandwich('ham', 'cheese', 'bacon')
make_sandwich('pepperoni', 'ham', 'butter')
make_sandwich('pindakaas', 'hagelslag', 'boter')


# program 2:
def show_magicians(magicians):
	'''function takes list of names, then prints each list element'''
	for magician in magicians:
		print(magician)

def make_great(magicians):
	'''function takes list of magicians, adds "The Great" for each
	list element, then returns a new list with updated list elements'''
	great_magicians = []
	while magicians:
		magician = magicians.pop() 
		great_magician = magician + " The Great"
		great_magicians.append(great_magician)
	
	for great_magician in great_magicians:
		magicians.append(great_magician)
	return great_magicians
	
magicians = ["pepe", "juan", "nacho", "luis"]
great_magicians = make_great(magicians[:])

print("Here are the results of show_magicians with the first list: ")
show_magicians(magicians)
print("Here are the results of show_magicians with the second list: ")
show_magicians(great_magicians)

# program 3:
def make_car(manufacturer, model, **extra_info):
	'''function takes multiple variable parameters, adds them to a newly
	created dictionary and returns that dictionary'''
	car_info = {}
	car_info['manufacturer'] = manufacturer
	car_info['model'] = model 
	for key, value in extra_info.items():
		car_info[key] = value
	return car_info

car = make_car('saburu', 'outback', color='blue', tow_package=True)
print(car)


