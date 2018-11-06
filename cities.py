'''Make a dictionary called cities. Use the names of three cities as keys
in your dictionary. Create a dictionary of information about each city 
and include the country that the city is in, its approximate population, and
one fact about that city. The keys for each city's dictionary should be 
something like country, population and fact. Print the name of each city and
all the information you have stored about it.'''

cities = {'Granada': 	{'country': 'Spain',
						'population': '65 million',
						'fact': 'has the Alhambra',
						},
		'Madrid':		{'country': 'Spain',
						'population': '65 million',
						'fact': 'capital of Spain'},
		'Amsterdam':	{'country': 'Holland',
						'population': '17 million',
						'fact': 'very cold'},
		}				

for city_name, city_info in cities.items():
	print("City: " + city_name)
	country = city_info['country']
	population = city_info['population']
	fact = city_info['fact']
	print("\nCountry: " + country, "\nPopulation: " + population, 
	"\nfact: " + fact)
