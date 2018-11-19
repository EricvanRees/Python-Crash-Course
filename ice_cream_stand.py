'''An icecream stand is a specific kind of restaurant. Write a class called
IceCreamStand that inherits from the restaurant class you wrote in 9-1 or 9-4.
Either version of the class will work; just pick the one you like better. Add
an attribute called flavors that stores a list of ice cream flavors. 
Write a method that displays these flavors. 
Create an instance of IceCreamStand, and call this method. '''

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
		
class IceCreamStand(Restaurant):
	'''Represents a specific kind of restaurant'''
	
	def __init__(self, restaurant_name, cuisine_type):
		'''Initialize attributes of parent class''' 
		super().__init__(restaurant_name, cuisine_type)
		'''attribute called flavors that stores a list
		 of ice cream flavors. '''
		self.flavors = ["banana", "strawberry", "oreo"] 
		
	def describe_flavors(self):
		'''print list of ice cream flavors'''
		for i in self.flavors:
			print(i)

# creating an instance of IceCreamStand
my_ice_cream_stand = IceCreamStand("IJskokar", "ijs")
# calling method that describes ice cream flavors
my_ice_cream_stand.describe_flavors()
