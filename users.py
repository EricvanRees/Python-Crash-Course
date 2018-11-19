'''Make a class called User. Create two attributes called first_name 
and last_name, and then create several other attributes that are usually
stored in a user profile. Make a method called describe_user() that prints
a summary of the user's information. Make another method called greet_user()
that prints a personalized greeting to the user. 
Create several instances representing different users, and call both methods
for each user.'''

class User():
	'''class that defines a user'''
	
	def __init__(self, first_name, last_name, age, gender):
		'''initialize first and last name of user, age and gender'''
		
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.gender = gender
		
	def describe_user(self):
		''' method that describes user'''
		print("Username: \t" + self.first_name + " " + self.last_name +
		"\nAge: " + self.age + "\tGender: " + self.gender)
		
	def greet_user(self):
		''' method that greets user'''
		print("Hello, " + self.first_name + " " + self.last_name + "!")
		
user1 = User("Eric", "van Rees", "38", "male")
user2 = User("Bill", "Gates", "65", "male")
user3 = User("Pablo", "Picasso", "144", "male")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
