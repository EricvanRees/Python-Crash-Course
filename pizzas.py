'''Think of at least three of your favorite pizzas.
Store them in a list and then use a for loop to print the name
of each pizza.'''

pizzas = ["diabolo", "frutti di mari", "calzone"]
for pizza in pizzas:
	print(pizza)
	
'''Modify your for loop to print a sentence using the name of the 
pizza instead of printing just the name of the pizza.'''

for pizza in pizzas:
	print("I like " + pizza + " pizza.")  

'''Add a line at the end of your program, outside the for loop,
that states how much you like pizza. '''

for pizza in pizzas:
	print("I like " + pizza + " pizza.")
print("I really love pizza!")
