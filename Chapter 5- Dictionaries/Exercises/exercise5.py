'''Chapter 5 Exercise 5: Pets '''


# Creating dictionaries for different pets
pet1 = {'Animal': 'dog', 'owner': 'Noor'}
pet2 = {'Animal': 'cat', 'owner': 'Dua'}
pet3 = {'Animal': 'Goat', 'owner': 'David'}
pet4 = {'Animal': 'rabbit', 'owner': 'Hessa'}

# Storing dictionaries in a list called pets
pets = [pet1, pet2, pet3, pet4]

# Looping through the list and printing information about each pet
for pet in pets:
    print("Kind of animal:", pet['Animal'])
    print("Owner's name:", pet['owner'])
    print()  # Adding an empty line for better readability
