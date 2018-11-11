'''make a list of magician's names. Pass the list to a function called
show_magicians(), that prints the name of each magician in the list.'''

magicians = ["pepe", "juan", "nacho", "luis"]
def show_magicians(a_list):
	for magician in magicians:
		print(magician)
		
show_magicians(magicians)
