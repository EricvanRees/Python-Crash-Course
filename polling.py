'''Use the code in favorite_languages.py.

* 1. Make a list of people who should take the favorite languages poll.
Include some names that are already in the dictionary and some that are not.

* 2. Loop through the list of people who should take the poll. If they have 
already taken the poll, print a message thanking them for responding. If they
have not yet taken the poll, print a message inviting them to take the poll.
'''

favorite_languages = {
						'jen': 'Python',
						'sarah': 'c',
						'edward': 'ruby',
						'phil': 'python',
						}
# 1
people = ['jen', 'phil', 'thom', 'pablo', 'kanye']

# 2
for i in people:
	if i in favorite_languages.keys():
		print("Hi " + i + ", thank you for responding.")
	else:
		print("Hi " + i + ", please take our poll.")

