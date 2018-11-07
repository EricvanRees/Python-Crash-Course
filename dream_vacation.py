'''Write a program that polls users about their dream vacation. 
Write a prompt similar to "If you could visit one place in the world,
where would you go?" Include a block of code that prints the results of the
poll.'''

responses = {}
polling_active = True

while polling_active:
	name = input("\nWhat is your name? ")
	response = input("Where would you if you could " +
	 "visit one place in the world? ")
	responses[name] = response 
	 
	repeat = input("Would you like to let another person respond? yes/no")
	if repeat == 'no':
		polling_active = False
	
print("\n---------POLLING RESULTS--------------")
for name, response in responses.items():
	print(name + " wants to visit:  " + response) 
