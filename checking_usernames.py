'''Do the following to create a program to create a program that simulates
how websites ensure that everyone has a unique username.

* make a list of five or more usernames called current_users
* make another list of usernames called new_users. Make sure one or two
of the new usernames are also in the current_users list.
* loop through the new_users list to see if each new username has already
been used.If it has, print a message that the user will need to enter a new
username. If a username has not been used, print a message saying that the
username is available.
* make sure your comparison is case-insensitive. If 'John' has been used,
'JOHN' should not be accepted.
'''

current_users = ["Maaike", "Peter", "Tom", "Nelleke", "Bert", "Ernie"]
new_users = ["Tom", "BERT", "Henk", "Bertje"]

for user in new_users:
	if user.title() in current_users:
		print(user + ", you will need to enter a new username.")
	else:
		print("Username " + user + " is available.")


