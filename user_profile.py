'''Start with a copy of user_profile.py
Build a profile of yourself by calling build_profile(), using your first
and last names and three other key-value pairs that describe you.'''

def build_profile(first, last, **user_info):
	'''Build a dictionary containing everything we know about the user'''
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

print(build_profile('Eric', 'van Rees', city='Granada', age='38', 
country='Spain'))