'''Imagine an alien was just shot down in a game. Create a variable called
"alien_color" and assign it a value of 'green', 'yellow' or 'red'. 

* Write an if statement to test whether the alien's color is green. If it is,
print a message that the player just earned five points.'''

alien_color = "red"
if alien_color == "green":
	print("You have just earned five points")
	
'''Write one version of this program that passes the if test and another
that fails. (The version that fails will have no output).'''

# program that passes the test
alien_color = "red"
if alien_color == "red":
	print("You have just earned five points")

# program that fails the test
alien_color = "red"
if alien_color == "green":
	print("You have just earned five points")
