'''Write an if-elif-else chain that determines a person's stage of life.
Set a value for the variable age, and then:

* if the person is less than two years old, print a message that the
person is a baby
* if the person is at least two years old but less than four, print a message
that the person is a toddler
* if the person is at least four years old but less than thirteen, print that
the person is a kid
* if the person is at least thirteen years old but less than twenty,
print a message that the person is a teenager
* if the person is at least twenty years old but less than sixty-five,
print a message that the person is an adult
* if the person is sixty-five or older, print a message that the person is 
an elder'''

age = 45
if age < 2:
	print("You are a baby")
elif age >= 2 and age < 4:
	print("You are a toddler")
elif age >= 4 and age < 13:
	print("You are a kid")
elif age >= 13 and age < 20:
	print("You are a teenager")
elif age >= 20 and age < 65:
	print("You are an adult")
elif age >= 65:
	print("You are an elder")
