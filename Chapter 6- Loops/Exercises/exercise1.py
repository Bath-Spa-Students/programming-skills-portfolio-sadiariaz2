''' Chapter 6 Exercise 1: Pizza Toppings '''



# Print a message prompting the user to enter pizza toppings
print("Enter pizza toppings. Type 'quit' to finish.")

# Run an infinite loop
while True:
     # Prompt the user to enter a topping
    topping = input("Enter a topping: ")
    
    # Check if the user input (converted to lowercase) is 'quit'
    if topping.lower() == 'quit':
          # If 'quit' is entered, exit the loop
        break
    # If the input is not 'quit', print a message indicating the topping will be added to the pizza
    print("I'll add", topping, "to your pizza.")