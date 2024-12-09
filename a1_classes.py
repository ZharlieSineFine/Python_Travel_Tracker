"""
CP1404/CP5632 Assignment 2 - Console program rewritten with Assignment 1 code and classes.
Name: Zhao Changlin
Date started: September 21st, 2023
"""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from place import Place
from placecollection import PlaceCollection
import random

MENU = "Menu:\nL - List places\nR - Recommend random place\nA - Add new place\nM - Mark a place as visited\nQ - Quit"
FILENAME = 'places.csv'
VALID_OPTIONS = ('L', 'R', 'A', 'M', 'Q')
CITY_INDEX = 0
COUNTRY_INDEX = 1
MARK_PLACE_PROMPT = "Enter the number of a place to mark as visited\n>>> "
PRIORITY_FIELD_WIDTH = 4


def main():
    """Combine classes and functions to make a travel tracker console program."""
    print("Travel Tracker 1.0 - by Zhao Changlin")
    place_collection = PlaceCollection()
    place_collection.load_places(FILENAME)
    place_collection.sort('is_visited')
    unvisited_places = extract_unvisited_places(place_collection.places)
    print(f"{determine_singular_or_plural(len(place_collection.places), 'place', 'places')} "
          f"loaded from {FILENAME}")

    print(MENU)
    user_option = get_valid_option()

    while user_option != 'Q':
        if user_option == 'L':
            display_places(place_collection.places)
            summarize_places(place_collection.places, unvisited_places)

        elif user_option == 'R':
            unvisited_places = extract_unvisited_places(place_collection.places)
            recommend_place(unvisited_places)

        elif user_option == 'A':
            city_name = get_valid_name("Name: ")
            country_name = get_valid_name("Country: ")
            place_priority = get_valid_priority("Priority: ")
            new_place = Place(city_name, country_name, place_priority, False)
            place_collection.add_place(new_place)
            print(f"{city_name} in {country_name} (priority {place_priority}) added to Travel Tracker")
            place_collection.sort('is_visited')
            unvisited_places = extract_unvisited_places(place_collection.places)

        else:  # user_option == 'M'
            if not unvisited_places:  # Check if unvisited_places is empty
                print("No unvisited places")
            else:
                display_places(place_collection.places)
                print(  # Similar to summarize_places function, but without displaying 'No place left' part
                    f"{len(place_collection.places)} places. You still want to visit "
                    f"{determine_singular_or_plural(len(unvisited_places), 'place', 'places')}.")
                number_to_place = {i: place for i, place in enumerate(place_collection.places, 1)}
                user_number = get_valid_number(number_to_place)
                number_to_place[user_number].mark_as_visited()
                place_collection.sort('is_visited')
                unvisited_places = extract_unvisited_places(place_collection.places)

        print(MENU)
        user_option = get_valid_option()

    place_collection.save_places(FILENAME)
    print(f"{determine_singular_or_plural(len(place_collection.places), 'place', 'places')} "
          f"saved to {FILENAME}\nHave a nice day :)")


def summarize_places(places, unvisited_places):
    """Summarize the current situation."""
    print(f"{len(places)} places.", end=' ')
    if unvisited_places:
        print(
            f"You still want to visit "
            f"{determine_singular_or_plural(len(unvisited_places), 'place', 'places')}.")
    else:
        print("No places left to visit. Why not add a new place?")


def recommend_place(unvisited_places):
    """Recommend a random place from unvisited places."""
    try:
        random_place = random.choice(unvisited_places)
        print("Not sure where to visit next?")
        print(f"How about... {random_place[CITY_INDEX]} in {random_place[COUNTRY_INDEX]}?")
    except IndexError:
        print("No places left to visit!")


def get_valid_number(number_to_place):
    """Get a valid user input number that match with one of the keys of the dictionary."""
    user_number = input(MARK_PLACE_PROMPT)
    is_valid_number = False
    while not is_valid_number:
        try:
            user_number = int(user_number)
            if user_number <= 0:
                print("Number must be > 0")
                user_number = input(">>> ")
            elif user_number not in number_to_place.keys():
                print("Invalid place number")
                user_number = input(">>> ")
            else:
                is_valid_number = True
        except ValueError:
            print("Invalid input; enter a valid number")
            user_number = input(">>> ")
    return user_number


def get_valid_priority(prompt):
    """Get a valid user input priority for the new place."""
    place_priority = input(prompt)
    is_valid_priority = False
    while not is_valid_priority:
        try:
            place_priority = int(place_priority)  # Convert input to integer
            if place_priority > 0:
                is_valid_priority = True  # If converted and priority > 0, it becomes True to exit the loop
            else:
                print("Priority has to be > 0")
                place_priority = input(prompt)
        except ValueError:
            print("Priority has to be an integer")
            place_priority = input(prompt)
    return place_priority


def get_valid_option():
    """Get a valid user input menu choice."""
    user_option = input(">>> ").upper()
    while user_option not in VALID_OPTIONS:
        print("Invalid menu choice")
        print(MENU)
        user_option = input(">>> ").upper()
    return user_option


def get_valid_name(prompt):
    """Get a valid name for cities and countries."""
    name = input(prompt).title()
    has_digit = False
    for char in name:
        has_digit = has_digit or char.isdigit()  # has_digit flag will stay True once a digit is found
    while name == '' or has_digit:
        if has_digit:
            print("Name cannot contain digits")
        else:
            print("Input can not be blank")
        name = input(prompt).title()
        has_digit = False  # Reinitialize the has_digit flag to False
        for char in name:
            has_digit = has_digit or char.isdigit()
    return name


def extract_unvisited_places(places):
    """Extract unvisited places from the list of places."""
    unvisited_places = [[place.name, place.country] for place in places if
                        not place.is_visited]
    return unvisited_places


def display_places(places):
    """Print lined up places information."""
    cities = [place.name for place in places]
    countries = [place.country for place in places]
    city_name_maximum_length = max(len(city) for city in cities)
    country_name_maximum_length = max(len(country) for country in countries)

    for i, place in enumerate(places, 1):
        start_literal = "*" if not place.is_visited else " "
        print(f"{start_literal}{i}. {place.name:<{city_name_maximum_length}} in"
              f" {place.country:<{country_name_maximum_length}} {place.priority:>{PRIORITY_FIELD_WIDTH}}")


def determine_singular_or_plural(number, singular_term, plural_term):
    """Determine the correct singular or plural form."""
    return f"{number} {singular_term}" if number == 1 else f"{number} {plural_term}"


if __name__ == '__main__':
    main()
