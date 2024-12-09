"""
Name: Zhao Changlin
Date: September 22nd, 2023
Brief Project Description: CP1404/CP5632 Assignment 2 - GUI program created with Kivy toolkit and classes.
GitHub URL: https://github.com/JCUS-CP1404/cp1404-travel-tracker-assignment-2-ZharlieSineFine
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from placecollection import PlaceCollection
from place import Place

KIVY_FILENAME = 'app.kv'
PLACES_FILENAME = 'places.csv'
RED_COLOR_CODE = [1, 0, 0, 1]
GREEN_COLOR_CODE = [0, 1, 0, 1]
TEXT_TO_ATTRIBUTE = {'Visited': 'is_visited', 'Priority': 'priority', 'Country': 'country', 'Name': 'name'}


class TravelTrackerApp(App):
    """TravelTrackerApp is a Kivy App that simulate a tracker for places to visit."""

    status_message = StringProperty()
    place_attributes = ListProperty()

    def __init__(self, **kwargs):
        """Construct the TravelTrackerApp object."""
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()

    def build(self):
        """Build Kivy GUI for TravelTrackerApp."""
        self.title = "TravelTracker"
        self.root = Builder.load_file(KIVY_FILENAME)
        self.place_collection.load_places(PLACES_FILENAME)
        self.place_collection.sort('is_visited')
        self.create_place_buttons()
        self.status_message = "Welcome to Travel Tracker 2.0"
        self.place_attributes = TEXT_TO_ATTRIBUTE.keys()
        return self.root

    def create_place_buttons(self):
        """Create dynamic place buttons."""
        self.root.ids.places_buttons.clear_widgets()
        for place in self.place_collection.places:
            button_color = RED_COLOR_CODE if place.is_visited else GREEN_COLOR_CODE
            visited_mark = '(visited)' if place.is_visited else ''
            temp_button = Button(text=f"{place.name} in {place.country}, priority {place.priority} {visited_mark}",
                                 background_color=button_color)
            temp_button.bind(on_release=self.press_place)
            self.root.ids.places_buttons.add_widget(temp_button)
        self.update_top_status()

    def sort_places(self):
        """Sort the places based on the selected text."""
        sort_text = self.root.ids.sort_key.text
        sort_attribute = TEXT_TO_ATTRIBUTE[sort_text]
        self.place_collection.sort(sort_attribute)

    def update_top_status(self):
        """Update the top status bar with the number of places left to visit."""
        number_of_unvisited = self.place_collection.get_number_of_unvisited_places()
        self.root.ids.top_status.text = f"Places to visit: {number_of_unvisited}"

    def press_place(self, instance):
        """Handle place buttons press event."""
        city_name = instance.text.split()[0]  # Get the city name from the button text
        for place in self.place_collection.places:
            if place.name == city_name:
                if place.is_visited:
                    place.mark_as_unvisited()
                    important_message = " Get going!" if place.is_important() else ""
                    self.status_message = f"You need to visit {city_name}.{important_message}"
                else:
                    place.mark_as_visited()
                    important_message = " Great travelling!" if place.is_important() else ""
                    self.status_message = f"You visited {city_name}.{important_message}"
        self.sort_places()
        self.create_place_buttons()

    def validate_input(self):
        """Check if the input is valid."""
        name = self.root.ids.name_input.text
        country = self.root.ids.country_input.text
        priority = self.root.ids.priority_input.text

        if not name or not country or not priority:
            self.status_message = "All fields must be completed"
            return False

        try:
            priority = int(priority)
        except ValueError:
            self.status_message = "Please enter a valid number"
            return False

        if priority <= 0:
            self.status_message = "Priority must be > 0"
            return False

        return True

    def add_place(self):
        """Add a new place object to the place collection."""
        if self.validate_input():
            name = self.root.ids.name_input.text.title()
            country = self.root.ids.country_input.text.title()
            priority = int(self.root.ids.priority_input.text)
            self.place_collection.add_place(Place(name, country, priority, False))
            self.clear_fields()
            self.status_message = f"{name} in {country}, priority {priority} added"

    def clear_fields(self):
        """Clear the text input fields and status message."""
        self.root.ids.name_input.text = ""
        self.root.ids.country_input.text = ""
        self.root.ids.priority_input.text = ""
        self.status_message = ""

    def handle_spinner_selection(self):
        """Handle the sort by spinner selection."""
        self.sort_places()
        self.create_place_buttons()

    def handle_add_place(self):
        """Handle the Add Place button click event."""
        if self.validate_input():
            self.add_place()
            self.sort_places()
            self.create_place_buttons()

    def on_stop(self):
        """Save the places to the CSV file when the program ends."""
        self.place_collection.save_places('places.csv')


if __name__ == '__main__':
    TravelTrackerApp().run()
