'''Start with your work from exercise 8-10. Call the function make_great()
with a copy of the list with magicians' names. Because the original list
will be unchanged, return the new list and store it in a separate list. 
Call show_magicians() with each list to show that you have one list of the
original names and one list with The Great added to each magician's name.'''

def show_magicians(magicians):
	'''function takes list of names, then prints each list element'''
	for magician in magicians:
		print(magician)

def make_great(magicians):
	'''function takes list of magicians, adds "The Great" for each
	list element, then returns a new list with updated list elements'''
	great_magicians = []
	while magicians:
		magician = magicians.pop() 
		great_magician = magician + " The Great"
		great_magicians.append(great_magician)
	
	for great_magician in great_magicians:
		magicians.append(great_magician)
	return great_magicians
	
magicians = ["pepe", "juan", "nacho", "luis"]
great_magicians = make_great(magicians[:])

print("Here are the results of show_magicians with the first list: ")
show_magicians(magicians)
print("Here are the results of show_magicians with the second list: ")
show_magicians(great_magicians)
