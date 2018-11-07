'''Write different versions of 7.4 and 7.5 that do each of the 
following at least once:

* use a conditional test in the while statement to stop the loop.
* use an active variable to control how long the loop runs.
* use a break statement to exit the loop when the user enters a 'quit'
value.''' 

'''# 7.4 rewritten  
prompt = "Enter a series of pizza toppings or 'quit'"
message = ""
i = 0

while message != 'quit':
	
	message = input(prompt)
	
	if message != "quit":
		print(message + " added to pizza.")
		i+= 1
		print(str(i) + " topping(s) added.")
		continue
	else:
		break
'''
# 7.5 rewritten
prompt = "Enter your age or 'quit' to stop. "
message = ""
i = 0

while message != 'quit':
	message = input(prompt)
	
	if message != 'quit':
		age = int(message)
		if age < 3:
			print("Your ticket is free")
			i += 1
			print(str(i) + " iterations of loop.")
		elif age > 3 and age < 12:
			print("Your ticket is $10")
			i += 1
			print(str(i) + " iterations of loop.")
		else:
			print("Your ticket is $15")
			i += 1
			print(str(i) + " iterations of loop.")
	elif message == 'quit':
		print("Quitting...")
		break
	else:
		break
