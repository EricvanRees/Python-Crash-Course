'''Write a function called describe_city() that accepts the name of a city
and its country. The function should print a simple message, such as
Reykjavik is in Iceland. Give the paramater for the country a default value.
Call your function for three different cities, at least one that is not
in the default country.'''

def describe_city(city, country="Spain"):
		print(city + " is in " + country)
	
describe_city("Malaga")
describe_city("Granada")
describe_city("Asterdam", "Holland")

