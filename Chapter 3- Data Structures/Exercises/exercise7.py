'''Chapter 3 Exercise 7: Seeing the World'''

# Define a list of places to visit
places_to_visit = ["Turkey", "Saudi Arabia", "Bahrain", "Canada", ""]
# Print the original order of the list
print("Original order:", places_to_visit)

# Print the list in alphabetical order without modifying the original list
print("Alphabetical order:", sorted(places_to_visit))

# Print the original order of the list to show that it remains unchanged after using
print("Original order after sorted():", places_to_visit)

# Print the list in reverse alphabetical order without modifying the original list
print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))

# Print the original order of the list to show that it remains unchanged after using sorted() with reverse=True
print("Original order after sorted(reverse=True):", places_to_visit)
# Reverse the order of the list in place
places_to_visit.reverse()
print("Reversed order:", places_to_visit)
# Reverse the order of the list back to its original order in place
places_to_visit.reverse()
print("Original order after reversing again:", places_to_visit)
# Sort the list in alphabetical order in place
places_to_visit.sort()
print("Alphabetical order after sort():", places_to_visit)
# Sort the list in reverse alphabetical order in place
places_to_visit.sort(reverse=True)
print("Reverse alphabetical order after sort(reverse=True):", places_to_visit)
