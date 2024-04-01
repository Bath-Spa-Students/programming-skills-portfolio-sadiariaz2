'''Chapter 6 Exercise 5: No Pastrami'''


# List of sandwich orders
sandwich_orders = ["ham and cheese", "pastrami", "turkey", "pastrami", "veggie", "pastrami", "grilled chicken"]
# List to store finished sandwiches
finished_sandwiches = []

# Print a message indicating that the deli has run out of pastrami
print("Sorry, the deli has run out of pastrami.")

# Remove all instances of "pastrami" from the sandwich orders list
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
# Process each sandwich order until there are no orders left
while sandwich_orders:
# Get the first sandwich order from the list
    current_sandwich = sandwich_orders.pop(0)
      # Print a message indicating that the current sandwich has been made
    print("I made your", current_sandwich, "sandwich.")
        # Add the current sandwich to the list of finished sandwiches
    finished_sandwiches.append(current_sandwich)
# Print the list of finished sandwiches
print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)

