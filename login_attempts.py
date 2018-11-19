'''Add an attribute called login_attempts to your User calls from 
Exercise 9.3. Write a method called login_attempts() that increments
the value of login_attempts by 1. Write another method called reset_login_
attempts() that resets the value of login_attempts to 0. 
Make an instance of the User class and call increment_login_attempts() 
several times. Print the value of login_attempts to make sure it was
incremented properly, and then call reset_login_attempts(). Print 
login_attempts again to make sure it was set to 0.'''

class User():
	'''class that defines a user'''
	
	def __init__(self, first_name, last_name, age, gender):
		'''initialize first and last name of user, age and gender'''
		
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.gender = gender
		self.login_attempts = 0
		
	def describe_user(self):
		''' method that describes user'''
		print("Username: \t" + self.first_name + " " + self.last_name +
		"\nAge: " + self.age + "\tGender: " + self.gender)
		
	def greet_user(self):
		''' method that greets user'''
		print("Hello, " + self.first_name + " " + self.last_name + "!")
		
	def increment_login_attempts(self):
		'''method that increments login attempts''' 
		self.login_attempts += 1
		print("Number of login attempts: " + str(self.login_attempts))
		
	def reset_login_attempts(self):
		'''method that resets login attempts to zero'''
		self.login_attempts = 0
		
my_user = User("Paul", "de Munnick", "56", "male")
my_user.increment_login_attempts() # returns 1
my_user.increment_login_attempts() # returns 2
my_user.increment_login_attempts() # returns 3
my_user.increment_login_attempts() # returns 4
my_user.reset_login_attempts() # sets login_attempts to 0
my_user.increment_login_attempts() #returns 1

