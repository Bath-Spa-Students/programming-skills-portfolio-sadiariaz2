'''Capter 6  Exercise 2: Movie Tickets'''

# Run an infinite loop to continuously prompt the user for their age
while True:
    # Prompt the user to enter their age (or type 'quit' to exit)
    age = input("Please enter your age (or type 'quit' to exit): ")
     # Check if the user wants to quit
    if age.lower() == 'quit':
        # Exit the loop if the user wants to quit
        break
       # Convert the user input to an integer
age= int(age)
if age < 3:  # Determine ticket cost based on age
        print("Your ticket is free.") # Print message if age is less than 3
elif 3<= age <=12:
   print("Your ticket Cost $10.")  # Print message if age is between 3 and 12 (inclusive)
else:
     print( "Your ticket costs $ 15.") # Print message for all other ages






