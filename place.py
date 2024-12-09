"""CP1404/CP5632 Assignment 2 - Place class.
"""


# Create your Place class in this file


class Place:
    """Represent a place object with information."""

    def __init__(self, name="", country="", priority=0, is_visited=False):
        """Construct a Place object with provided attributes."""
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        """Return the string form of Place class."""
        return f"{self.name} in {self.country}, priority {self.priority}, visited or not: {self.is_visited}."

    def mark_as_visited(self):
        """Mark a place as visited."""
        self.is_visited = True

    def mark_as_unvisited(self):
        """Mark a place as unvisited."""
        self.is_visited = False

    def is_important(self):
        """Determine if a place is considered important(priority <= 2)."""
        return self.priority <= 2
