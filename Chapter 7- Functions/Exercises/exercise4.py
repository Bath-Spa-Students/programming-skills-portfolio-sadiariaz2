'''Chapter 7 Exercise 4:  Large Shirts '''

# Define a function called make_shirt with two parameters: size and message, both of which have default values
def make_shirt(size="large", message="I love Python"):
    """Prints a sentence summarizing the size of the shirt and the message printed on it."""
    # Print a sentence summarizing the size of the shirt and the message
    print(f"A {size}-sized shirt will be made with the message: '{message}'.")
# Call the make_shirt function with default values for size and message
make_shirt()
# Call the make_shirt function with size="medium" and the default message
make_shirt(size="medium")

# Call the make_shirt function with size="small" and message="I'm the BOSS"
make_shirt(size="small", message= "I'm the BOSS")

