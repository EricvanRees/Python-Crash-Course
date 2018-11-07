'''write a loop that prompts the user to enter a series of pizza toppings
until they enter a 'quit' value. As they enter each topping, print a message
saying that you'll add that topping to their pizza.'''

prompt = "Enter a series of pizza toppings or 'quit'"
message = ""

while message != 'quit':
	
	message = input(prompt)
	
	if message != "quit":
		print(message + " added to pizza.")
		continue
	else:
		break
