'''Write a function called make_shirt() that accepts the size and the text
of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make the shirt.
Call the function a second time using keyword arguments.'''

def make_shirt(size, text):
	print("shirt size is: " + size)
	print("shirt text is: " + text)
	
# function call using positional arguments
make_shirt("xl", "Sonic Youth") 

# function call using keyword arguments
make_shirt(size='xl', text='Sonic Youth')
