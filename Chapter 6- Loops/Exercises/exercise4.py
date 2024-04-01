'''Chapter 6: Exercise 4: Deli'''


# List of sandwich orders
sandwich_orders = ["ham and cheese", "turkey", "veggie", "grilled chicken"]

# List to store finished sandwiches
finished_sandwiches = []

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

