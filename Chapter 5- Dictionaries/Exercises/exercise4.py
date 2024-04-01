'''Chapter 5 Exercise 4: Rivers'''


rivers={
     'Amazon River': ' South America',
     'Danube River': 'European',
     'Thames River': 'London',
     'Congo River': 'Africa',
}
# Print each river and the continent or country it runs through
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# Print section header indicating the start of river names
    print("\nRivers:")
    #print each river name
for river in rivers.keys():
    print(river)
# Print section header indicating the start of countries
    print("\nCountries:")
    
# Print each continent or country
for country in rivers.values():
    print(country)