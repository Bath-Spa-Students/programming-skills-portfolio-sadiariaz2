"""Chapter2 Exercise 3 Stripping Names """

# Assigning a string with leading and trailing whitespace to the variable 'name'
name="\t Sadia\n"
# Print a message
print ("fani bu duniya")
# Print the value of the 'name' variable
print(name)
# Using lstrip() to remove leading whitespace
print("\nusing lstrip():")
print(name.lstrip())

# Using rstrip() to remove trailing whitespace
print("\nusing rstrip():")
print(name.rstrip())

# Using strip() to remove both leading and trailing whitespace
print("\nusing strip ():")
print(name.strip())