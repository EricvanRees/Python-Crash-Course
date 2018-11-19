''' Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings described in
Exercise 9-7. Move the show_privileges() method to this class. Make a 
privileges instance as an attribute in the Admin class. Create a new instance
of Admin and use your method to show its privileges.'''

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

class Admin(User):
	'''class that inherits from User class'''
	
	def __init__(self, first_name, last_name, age, gender):
		'''Initialize attributes of parent class'''
		super().__init__(first_name, last_name, age, gender)
		self.privileges = Privileges()
		

class Privileges():
	'''Class that defines privileges'''
	
	def __init__(self, privileges=[]):
		self.privileges = ["can add post", "can delete post", 
								"can ban user"]
	
	def show_privileges(self):
		for i in self.privileges:
			print(i)


my_admin = Admin("Harry", "Partch", "45", "male")
my_admin.privileges.show_privileges()
