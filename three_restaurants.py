'''Start with your class from Exercise 9-1. Create three different
instances of the class, and call describe_restaurant() for each instance.'''

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
		

my_restaurant1 = Restaurant("Bodega Castañeda", "Spanish")
my_restaurant2 = Restaurant("Casa de Maria", "Italian")
my_restaurant3 = Restaurant("El parador", "Spanish")

my_restaurant1.describe_restaurant()
my_restaurant2.describe_restaurant()
my_restaurant3.describe_restaurant()
