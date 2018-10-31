'''You have just found out that your new dinner table 
won't arrive in time for the dinner, and you only have space for two
guests. Start with your program from 3.6 and add a new line that prints
a message that you can only invite two people for dinner.'''

guests = ["Frank", "Paul", "Lisa", "Elvis", "Marthijn"]

def invitation(a):
	i = 0
	for a in guests:
		if guests[i] != "Lisa":
			print("Welcome to dinner " + guests[i])
			i+=1
		else:
			print(guests[2] + " can't make it")
			i+=1
	print("I only can invite two people for dinner.")

invitation(guests)

'''Use pop() to remove guests from your lists until two names remain
in your list. Each time you pop a name from your list, print a message
to that person letting them know you're sorry you can't invite them
to dinner.'''

not_welcome = guests.pop()
print("I'm sorry I can't invite you to dinner, " + not_welcome)
not_welcome = guests.pop()
print("I'm sorry I can't invite you to dinner, " + not_welcome)
not_welcome = guests.pop()
print("I'm sorry I can't invite you to dinner, " + not_welcome)

'''Print a message to each of the two people still on your list,
and let them know they're still invited.'''

message = "You're still invited, "
print(message + guests[0])
print(message + guests[1])

'''Use del() to remove the last two names from your list, so you have
an empty list. Print your list so you make sure you have actually and
empty list at the end of your program.'''

del guests[1]
del guests[0]
print("This is an empty list: " + str(guests))
