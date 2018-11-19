'''Start with your program from Excersise 9-1. Add an attribute called
number_served with a default value of 0. Create an instant called
restaurant from this class. Print the number of customers the restaurant has
served, and then change this value and print it again. 
Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and
print the value again. 
Add a method called increment_number_served() that lets you increment the
number of customers who have been served. Call this method with any number
you like that could represent how many customers were served in, say, a day
of business.'''

class Restaurant():
	'''A class to model a restaurant'''
	
	def __init__(self, restaurant_name, cuisine_type):
		'''initialize restaurant name and cuisine type'''
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 12
		
	def describe_restaurant(self):
		'''method to describe restaurant name and cuisine type'''
		print("This restaurant is called " + self.restaurant_name + 
					" and its cuisine type is " + self.cuisine_type + ".")

	def open_restaurant(self):
		print("The restaurant is open!")
		
	def set_customer_served(self, served_cust):
		'''method to set the number of customers served'''
		self.number_served = served_cust
		
	def increment_number_served(self, number):
		'''method to increment the number of served customers'''
		self.number_served += number 

'''Create an instant called restaurant from this class. 
Print the number of customers the restaurant has
served, and then change this value and print it again.'''
 
my_rest = Restaurant("Los Marines", "Spanish")
print("Number of customers served: " + str(my_rest.number_served))
my_rest = Restaurant("Los Marines", "Spanish")
print("Number of customers served: " + str(my_rest.number_served))

'''Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and
print the value again.'''

my_rest.set_customer_served(44)
print("Number of customers served: " + str(my_rest.number_served))

'''Add a method called increment_number_served() that lets you increment the
number of customers who have been served. Call this method with any number
you like that could represent how many customers were served in, say, a day
of business.'''

my_rest.increment_number_served(12)
print("Number of customers served in a day: " + str(my_rest.number_served))
