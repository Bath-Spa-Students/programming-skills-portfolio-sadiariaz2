'''Chapter 7 Exercise 5: Cities'''
# Define a function called describe_city with two parameters: city and country, with a default value of "Iceland" for country
def describe_city(city, country="Iceland"):
    """Prints a simple sentence describing the city and its country."""
    print(f"{city} is in {country}.")

# Call the function for three different cities
describe_city("Reykjavik")
describe_city("New York", "USA")
describe_city("Tokyo", "Japan")
describe_city("Istanbul", "Turkey")