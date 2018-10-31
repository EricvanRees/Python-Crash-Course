'''Think of something you can store in a list. 
Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.'''

cities = ["Salamanca", "Madrid", "Granada", "Sevilla"]

# modifying an element of a list:
cities[0] = "Cuenca"
print(cities)

# adding an element to a list:
cities.append("Zaragoza")
print(cities)
cities.insert(1, "Almeria")
print(cities)

# deleting an element from a list:
del cities[0]
print(cities)

# removing the last element from a list:
cities.pop()
print(cities)

# pop an item from any position:
cities.pop(0)
print(cities)

# removing an item by value:
cities.remove("Madrid")
print(cities)

# adding items:
cities.insert(0, "Madrid")
cities.insert(1, "Almeria")
print(cities)

# sorting a list permanently:
cities.sort()
print(cities)

# printing a list in reverse order:
cities.reverse()
print(cities)

# finding the length of a list:
print(len(cities))
