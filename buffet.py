'''A buffet-style restaurant only offers five basic foods.
Think of five basic foods, and store them in a tuple.

1. Use a for loop to print each food the restaurant offers.

2. Try to modify one of the items, and make sure that Python rejects
the change.

3. The restaurant changes its menu, replacing two of the items with
different foods. Add a block of code that rewrites the tuple,
and then use a for loop to print each of the items on the revised
menu.'''

#1
foods = ("hamburgers", "tacos", "fries", "bacon", "eggs")
for food in foods:
	print(food)

#2: creates TypeError: 'tuple' object does not support item assignment
#foods[0] = "fish and chips" 

#3
foods = ["donuts", "pancakes", "fries", "bacon", "eggs"]
print("\nRevised menu:")
for food in foods:
	 print(food)
