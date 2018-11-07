'''A movie theater charges different ticket prices based on someone's age.
If a person is under the age of three, the ticket is free; if they are
between 3 and 12, the ticket is $10, and if they are over 12, the ticket is
$15. Write a loop in which you ask the user's their age, and tell them the
cost of their movie ticket.'''

message = "How old are you? "
age = int(input(message))

if age < 3:
	print("Your ticket is free")
elif age > 3 and age < 12:
	print("Your ticket is $10")
else:
	print("Your ticket is $15")
