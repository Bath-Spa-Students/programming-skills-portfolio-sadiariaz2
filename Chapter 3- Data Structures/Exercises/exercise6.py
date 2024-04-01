''' Chapter 3 Exercise 6: Shrinking Guest List'''


guests = ['Waseem','George','Lara','Julia']


print("Sorry , I can only invite two people for dinner.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print("Sorry", removed_guest + ", I'm unable to invite you to dinner.")

# Print a message to each of the two people still on your list, letting them know they're still invited
for guest in guests:
    print("Dear", guest +  ", you're still invited to dinner.")

# Use del to remove the last two names from your list, so you have an empty list
del guests[:]


print("List of guests after dinner:", guests)
