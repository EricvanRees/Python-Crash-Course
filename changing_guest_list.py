'''Start with your program from 3.4. Add a print statement at
the end of your program stating the name of the guest
who can't make it'''

guests = ["Frank", "Paul", "Lisa"]

def invitation(a):
	i = 0
	for a in guests:
		if guests[i] == "Frank" or guests[i] == "Paul":
			print("Welcome to dinner " + guests[i])
			i+=1
		else:
			print(guests[2] + " can't make it")

invitation(guests)
		
'''Modify your list, replacing the name of the guest who can't make it
with the name of the new person you're inviting'''

guests.remove("Lisa")
guests.append("Peter")

'''Print a second set of invitation messages, one for each person who
is still on your list.'''
invitation(guests)


