'''Clean up your code from glossary.py by replacing your series of print
statements with a loop that runs through the dictionary's keys and values.
When you´re sure your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in your output.'''

glossary =	{'list': 'list of items enclosed with []',
			'dictionary': 'list of key/value pairs enclosed with {}',
			'for loop': 'looping construction in Python',
			'function': 're-usable code named as function',
			'if-elif-else statement': 'runs code based on conditions',
			'.items()': 'dictionary method for printing keys and values',
			'.keys()': 'method for printing dict keys',
			'.values()': 'method for printing dict values',
			'\ t': 'method for printing tabs when printing strings'}

for key, values in glossary.items():
	print(key + " : " + values) 
