'''Start with a copy of your program from Exercise 8-9. Write a function
called make_great() that modifies the list of magicians by adding the
phrase The Great to each magician's name. Call show_magicians() to see that
the list has acually been modified.'''


def show_magicians(magicians):
	for magician in magicians:
		print(magician)

def make_great(magicians):
	great_magicians = []
	while magicians:
		magician = magicians.pop() 
		great_magician = magician + " The Great"
		great_magicians.append(great_magician)
	
	for great_magician in great_magicians:
		magicians.append(great_magician)

magicians = ["pepe", "juan", "nacho", "luis"]
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)
