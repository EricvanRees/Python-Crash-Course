'''Using one of the programs you wrote in this chapter, add
several lines to the end of the program that do the following: 

1. print the message: "The first three items of the list are: ", 
Then use a slice to print the first three items from that program's 
list.

2. print the message: "Three items of the middle of the list are: ".
Use a slice to print three items from the middle of the list.

3. print the message: "The last three items of the list are: ".
Use a slice to print the last three items of the list.'''

#1
cubes = [value**3 for value in range(1,11)]
print("The first three items in the list are: " + str(cubes[:3]))

#2
print("Three items in the middle of the list are: " + str(cubes[5:8]))

#3
print("The last three items of the list are: " + str(cubes[-3:]))
