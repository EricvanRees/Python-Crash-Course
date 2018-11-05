'''Make a list of five or more usernames, including the name 'admin'.
Imagine that you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting
to each user:

* if the username is 'admin', print a special greeting, "Hello admin,
would you like to see a status report?"

* otherwise, print a generic greeting, such as "Hello Eric, thank you 
for logging in again" '''

usernames = ['Eric', 'admin', 'Paco', 'Elon Musk', 'Sheldon Cooper']
for username in usernames:
	if username == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print("Hello " + username + ", thank you for loggin in again.")
