'''Think of five programming words you've learned in the previous chapters.
Use these words as keys in your glossary, and store their meanings as
values. 
Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning pair
in your output.'''

glossary =	{'list': 'list of items enclosed with []',
			'dictionary': 'list of key/value pairs enclosed with {}',
			'for loop': 'looping construction in Python',
			'function': 're-usable code named as function',
			'if-elif-else statement': 'runs code based on conditions',}

print("A list is a " + glossary['list'] + 
		"\nA dictionary is a" + glossary['dictionary'] +
		"\nA for loop is a " + glossary['for loop'] + 
		"\nA function is a " + glossary['function'] + 
		"\nAn if-elif-else statement " + glossary['if-elif-else statement'])
