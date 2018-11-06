'''Make several dictionaries, where the name of each dictionary is the 
name of a pet. In each dictionary, include the kind of animal and the owner's
name. Store these dictionaries in a list called pets. Next, loop through your
list and as you do print everything you know about each pet.'''

kira = {'kind_of_animal': 'dog',
		'name_owner': 'Regina',}
ollie = {'kind_of_animal': 'cat',
		'name_owner': 'Gert',}
bertje = {'kind_of_animal': 'lizard',
		'name_owner': 'none',}
	
pets = [kira, ollie, bertje]

for i in pets:
	print("Kind of animal: " + i['kind_of_animal'])
	print("Name of owner: " + i['name_owner'])
