'''Write a function that accepts a list of items a person wants on a 
sandwich. The function should have one parameter that collects as many
items as the function call provides and it should print a summary of the
sandwich that´s being ordered. Call the function three times, using a 
different number of arguments each time.'''

def make_sandwich(*ingredients):
	'''function takes multiple parameters ,
	creates a sandwich of all parameters, then prints all parameters'''
	print("Your sandwich has: ")
	for ingredient in ingredients:
		print("-" + ingredient)	

make_sandwich('ham', 'cheese', 'bacon')
make_sandwich('pepperoni', 'ham', 'butter')
make_sandwich('pindakaas', 'hagelslag', 'boter')
