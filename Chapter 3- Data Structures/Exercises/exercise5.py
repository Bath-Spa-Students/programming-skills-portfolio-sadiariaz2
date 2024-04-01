
''' Chapter 3 Exercise 5: Change Guest List '''


# Initial list of guests
guests = ['Waseem','George','Lara','Julia']

# Removing the guest who can't make it to dinner and storing their name
guest_cant_make_it = guests.pop(1)  
print(f"Unfortunately, {guest_cant_make_it} can't make it to dinner.\n")
# Adding a new guest to the list
new_guest = "Angelina"
guests.append(new_guest)

# Removing another guest who can't make it to dinner and storing their name
guest_cant_make_it = guests.pop(3)
print(f"Unfortunately, {guest_cant_make_it} can't make it to dinner.\n")
# Adding another new guest to the list
new_guest = "Zack"
guests.append(new_guest)

# Printing invitations for each remaining guest
for guest in guests:
    print(f"Dear {guest},\nYou are invited to dinner at my place.It would be an honor to have you join us.\n\nSincerely,\n Sadia")
    print("\n")













