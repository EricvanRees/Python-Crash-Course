'''Turn your if-else chain into an if-elif-else chain.

*If the alien is green, make sure that the player earned five points.
* If the alien is yellow, print a message that the player earned ten points.
* If the alien is red, print a message that the player earned fifteen points.
* Write three versions of this program, making sure each message is printed
for the appropriate color alien.'''

# v1 
alien_color = "green"

if alien_color == "green":
	print("You just earned five points")
elif alien_color == 'yellow':
	print("You have just earned ten points")
else:
	print("You have just earned fifteen points")

#v2 
alien_color = "yellow"

if alien_color == "green":
	print("You just earned five points")
elif alien_color == 'yellow':
	print("You have just earned ten points")
else:
	print("You have just earned fifteen points")
	
#v3
alien_color = "red"
if alien_color == "green":
	print("You just earned five points")
elif alien_color == 'yellow':
	print("You have just earned ten points")
else:
	print("You have just earned fifteen points")
