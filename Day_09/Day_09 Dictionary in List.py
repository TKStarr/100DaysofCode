country = input("Enter the name of the country.")  # Add country name
visits = int(input("How many times have you been?"))  # Number of visits
list_of_cities = eval(input("Enter the cities you have been to.  Put quotation marks around each city and separate them with a space and a comma."))  # create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# Do NOT change the code above 👆

# Write the function that will allow new countries
# to be added to the travel_log.
def add_new_country(country, visits, list_of_cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = list_of_cities
    travel_log.append(new_country)


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")