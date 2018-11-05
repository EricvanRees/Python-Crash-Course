'''Write a series of conditional tests. Print a statement describing
each test and your prediction of the results of each test. Create
at least ten tests. Have at least five tests evaluate to True and 
five tests evaluate to False.'''

food = 'pizza'
print('Is food pizza? I predict True')
print(food == 'pizza')

car = 'Ford'
print('Is car Ford? I predict True')
print(car == 'Ford')

guitar = 'Fender'
print('Is guitar Fender? I predict True')
print(guitar == 'Fender')

book = 'Don Delillo'
print('Is book Don Delillo? I predict True')
print(book == 'Don Delillo')

device = 'iPod'
print('Is device iPod? I predict True')
print(device == 'iPod')

paper = 'NRC'
print('Is paper Volkskrant? I predict False')
print(paper == 'volkskrant')

beer = 'Alhambra'
print('Is beer Cruzcampo? I predict False' )
print(beer == 'Cruzcampo')

beer = 'Brugse Tripel'
print('Is beer Alhambra? I predict False')
print(beer == 'Alhambra')

magazine = 'El Pais'
print('Is magazine ABC? I predict False')
print(magazine == 'ABC')

room = 'kitchen'
print('Is room salon? I predict False')
print(room == 'salon')

'''Have at least one False and one True for each of the following:

* Tests with equality and inequality with strings
* Tests using the lower() function
* Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to.
* Tests using the "And" keyword and the "or" keyword
* Test whether an item is in a list.
* Test whether an item is not in a list.'''

# string equality
my_string = "hi"
your_string = "hi"
print(my_string == your_string)

# string inequality
my_string = "bla"
your_string = "bo"
print(my_string != your_string)

#test using the lower function resulting in True
my_string = "Mark"
print(my_string.lower() == "mark")

# test using the lower function resulting in False
my_string = "Eric"
print(my_string.lower() == "Eric")

#numerical tests involving equality
a = 8
b = 8
print(a == b)

a = 8
b = 9
print(a == b)

# numerical tests involving inequality
a = 8
b = 7
print(a != b)

a = 8
b = 8
print( a != b)

# numerical tests involving greater than and less than
a = 8
b = 9 
print(b > a) #true
print(a > b) #false
print(a < b) #true
print(b < a) #false

# greater than or equal to, less than or equal to
print(b >= a) #true
print(a >= b) # false
print(a <= b) #true
print(b <= a) #false
 
# tests using the "and" or the "or" keyword
print(a < 9 and b < 10) #true
print(a > 9 and b > 10) #false
print(a < 9 or b < 10) #true
print(a > 9 or b > 9) #false

# test whether an item is in a list
my_list = [1,2,3,4,5,6]
print(1 in my_list) #true

# test whether an item is not in a list
print(89 in my_list) #false


