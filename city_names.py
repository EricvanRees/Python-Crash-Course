'''Write a function named city_country() that takes in the name of a city
and its country. The function should return a string formatted like this:
"Santiago, Chile". Call your function with at least three city-country pairs,
and print the value that's returned.'''

def city_country(city, country):
	pair = (city + ", " + country)
	return pair
	
print(city_country("Granada", "Spain"))
print(city_country("Madrid", "Spain"))
print(city_country("Valladolid", "Spain"))
