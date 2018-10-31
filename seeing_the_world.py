'''Think of at least five different places you want to vist. 
Store the locations in a list. Make sure the list is not in 
alphabetical order.'''

places = ["Japan", "China", "Chile", "California", "New York"]

'''Print your list in its original order.'''

print(places)

'''Use sorted() to print your list in alphabetical order without
modifying the actual list.'''

print(sorted(places))

'''Show that your list is still in its original version by 
printing it.'''

print(places)

'''Use sorted() to print your list in reverse 
alphabetical order without changing the order of the original
list.'''

print(sorted(places, reverse=True)) 

'''Show that your list is still in its original order by printing 
it again.'''

print(places)

'''Use reverse() to change the order of your list. Print the list
to show that its order has changed.'''

places.reverse()
print(places)

'''Use reverse() to change the order of the list again. Print the list
to show the order has been changed.'''

places.reverse()
print(places)

'''Use sort() to change your list so it's stored in alphabetical order.
Print the list to show the order has been changed.'''

places.sort()
print(places)

