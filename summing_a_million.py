'''Make a list of the numbers one to a million, and then use
min() and max() to make sure your list actually starts at one and ends
at one million. Also, use the sum() function to see how quickly 
Python can add a million numbers.'''

my_list = list(range(1,100001))
print(min(my_list))
print(max(my_list))
print(sum(my_list))
