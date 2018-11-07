'''Ask the user for a number, and then report of the number is a multiple of
ten or not.'''

number = int(input("Please enter a number: "))

if number % 10 == 0:
	print("Number is multiple of ten")
else:
	print("Number is not a multiple of ten") 
