'''Using the list sandwich_orders from Exercise 7-8, make sure the
sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli 
has run out of pastrami, and then use a while loop to remove all 
occurences of 'pastrami' from sandwich_orders. Make sure no pastrami
sandwiches end up in finished_sandwiches.'''

sandwich_orders = ['new york', 'cheese', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []
print("The deli has run out of pastrami!")

while sandwich_orders:
	while 'pastrami' in sandwich_orders:
		sandwich_orders.remove('pastrami')
		continue
	sandwich_ready = sandwich_orders.pop()
		
	print("I made your " + sandwich_ready + " sandwich.")
	finished_sandwiches.append(sandwich_ready)

print("The following sandwiches have been made: ")
for i in finished_sandwiches:
	print(i)
