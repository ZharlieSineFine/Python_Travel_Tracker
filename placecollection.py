"""CP1404/CP5632 Assignment 2 - PlaceCollection class."""

import csv
from place import Place
from operator import attrgetter

VISITED_STATUS = 'v'
UNVISITED_STATUS = 'n'
PRIORITY_INDEX = 2
VISIT_INDEX = 3
CITY_INDEX = 0
COUNTRY_INDEX = 1


# Create your PlaceCollection class in this file


class PlaceCollection:
    """Represent a PlaceCollection object with places stored within."""

    def __init__(self):
        """Construct a PlaceCollection object with a list of Place objects."""
        self.places = []

    def __str__(self):
        """Return the string representation of a PlaceCollection object."""
        return "\n".join(str(place) for place in self.places)

    def load_places(self, filename):
        """Load the places information from designated file and store them into the list of Place objects."""
        with open(filename, "r") as in_file:
            content_reader = csv.reader(in_file)
            for row in content_reader:
                visit_status = True if row[VISIT_INDEX] == VISITED_STATUS else False  # Convert to True or False
                current_place = Place(row[CITY_INDEX], row[COUNTRY_INDEX], int(row[PRIORITY_INDEX]), visit_status)
                self.places.append(current_place)

    def save_places(self, filename):
        """Save the list of Place objects in the designated file."""
        with open(filename, "w") as out_file:
            for place in self.places:
                visit_status = VISITED_STATUS if place.is_visited else UNVISITED_STATUS  # Convert back to 'v' or 'n'
                print(f"{place.name},{place.country},{str(place.priority)},{visit_status}", file=out_file)

    def add_place(self, new_place: Place):
        """Append the new Place object to the list of Places."""
        self.places.append(new_place)

    def sort(self, first_attribute):
        """Sort the list of Place objects by designated attribute, then by priority."""
        self.places.sort(key=attrgetter(first_attribute, 'priority'))

    def get_number_of_unvisited_places(self):
        """Count the number of unvisited places in the list of Place objects."""
        number_of_unvisited_places = 0
        for place in self.places:
            if not place.is_visited:
                number_of_unvisited_places += 1
        return number_of_unvisited_places
