'''
* store the numbers 1 to 9 in a list.
* loop through the list
* use an in-elif-else chain inside the loop to print the proper ordinal
ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th
8th 9th" and each result should be on a separate line.
'''

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
	if number == 1:
		print(str(number)+"st")
	elif number == 2:
		print(str(number)+"nd")
	elif number == 3:
		print(str(number)+"rd")
	else:
		print(str(number)+"rd") 
