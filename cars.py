'''Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It should
then accept an arbitrary number of keyword arguments. Call the function with
the required information and two other name-value pairs, such as color or 
an optional feature. Your function should work like a call for this one:

car = make_car('saburu', 'outback', color='blue', tow_package=True)

Print the dictionary that's returned to make sure all the information was
stored correctly.'''

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
