'''Choose a color for an alien and write an if-else chain.

* If the alien's color is green, print a statement that the player just
earned five points for shooting the alien.
* If the alien's color isn't green, print a statement that the player just
earned ten points.
* write one version of this program that runs the if block and another that
runs the else block. '''

# v1 program runs if block
alien_color = "green"

if alien_color == "green":
	print("You just earned five points")
else:
	print("You have just earned ten points")

#v2 program runs else block

alien_color = "red"
if alien_color == "green":
	print("You have just earned five points")
else:
	print("You have just earned ten points")
