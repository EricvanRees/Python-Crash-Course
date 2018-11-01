'''Make a copy of the list of pizzas and call it friend_pizzas.
Then, do the followoing:

1. Add a new pizza to the original list.
2. Add a different pizza to the list friend_pizzas
3. Prove that you have two different lists. Print the message: 
"My favorite pizzas are:", and then use a for 
loop to print the first list. Print the message, "My friend's 
favorite pizzas are:" and then use a for loop to print the second
list. Make sure each new pizza is stored in the appropriate list.'''

pizzas = ["diabolo", "frutti di mari", "calzone"]
friend_pizzas = pizzas[:]

#1
pizzas.append("margarita")
#2
friend_pizzas.append("bambini")
#3
print("My favorite pizzas are: ")
for i in pizzas:
	print(i)
	
print("My friend's favorite pizzas are: ")
for i in friend_pizzas:
	print(i)
