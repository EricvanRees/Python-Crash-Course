'''Make a class called Restaurant. The __init__() method for Restaurant
should store two attributes: a restaurant_name and a cuisine_type. Make a
method describe_restaurant() that prints these two pieces of information,
and a method called open_restaurant() that prints a message indicating 
that the restaurant is open.
Make an instance called restaurant from your class. Print the two 
attributes individually, and then call both methods.'''

class Restaurant():
	'''A class to model a restaurant'''
	
	def __init__(self, restaurant_name, cuisine_type):
		'''initialize restaurant name and cuisine type'''
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		'''method to describe restaurant name and cuisine type'''
		print("This restaurant is called " + self.restaurant_name + 
					" and its cuisine type is " + self.cuisine_type + ".")

	def open_restaurant(self):
		print("The restaurant is open!")
			

# make instance from class
my_restaurant = Restaurant("Los Marines", "mediterranian")
# print both attributes individually
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
# call both methods
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
