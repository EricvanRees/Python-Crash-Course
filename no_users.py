'''Add an if test to hello_admin.py to make sure the list of users is not
emptpy.'''

usernames = ['Eric', 'admin', 'Paco', 'Elon Musk', 'Sheldon Cooper']

def check_usernames(my_list):
	if usernames:
		for username in usernames:
			if username == 'admin':
				print("Hello admin, would you like to see a status report?")
			else:
				print("Hello " + username + ", thank you for loggin in again.")
	else:
		print("We need to find some users!")

'''if the list is empty, print the message "We need to find some users!" 
Remove all the users from the list and make sure the correct message is 
displayed'''

usernames = []
check_usernames(usernames)
