'''An administrator is a special kind of user. Write a class called Admin
that inherits from the User class you wrote in 9-3 or 9-5. Add an attribute,
privilage, that stores a list of strings like "can add post", "can delete post"
, "can ban user" and so on. 
Write a method called show_privilages() that lists the administrator's
set of privilages. Create an instance of Admin and call your method.'''

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
		self.privileges = ["can add post", "can delete post", 
								"can ban user"]		
	def show_privileges(self):
		for i in self.privileges:
			print(i)
			
# creating instance of Admin:
my_admin = Admin("Sheldon", "Cooper", "23", "male")
# calling method show_privileges():
my_admin.show_privileges()
