'''Make a list called sandwich_orders and fill it with the name of various
sandwiches. Then make a list called finished_sandwiches. Loop through the
list of sandwich orders and print a message for each order, such as
"I made your tuna sandwich". As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.'''

sandwich_orders = ['new york', 'cheese', 'bacon', 'american', 'italian']
finished_sandwiches = []

while sandwich_orders:
	sandwich_ready = sandwich_orders.pop()
	
	print("I made your " + sandwich_ready + " sandwich.")
	finished_sandwiches.append(sandwich_ready)
print("The following sandwiches have been made: ")
for i in finished_sandwiches:
	print(i)
