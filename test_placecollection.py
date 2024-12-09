"""(Incomplete) Tests for PlaceCollection class."""
from placecollection import PlaceCollection
from place import Place


def run_tests():
    """Test PlaceCollection class."""

    # Test empty PlaceCollection (defaults)
    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.places  # an empty list is considered False

    # Test loading places
    print("Test loading places:")
    place_collection.load_places('places.csv')
    print(place_collection)
    assert place_collection.places  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Place with values
    print("Test adding new place:")
    place_collection.add_place(Place("Smithfield", "Australia", 5, False))
    print(place_collection)

    # Test adding other places
    print("Test adding other places:")
    place_collection.add_place(Place("Qingdao", "China", 2, True))
    place_collection.add_place(Place("Seattle", "United States", 3, True))
    print(place_collection)

    # Test sorting places
    print("Test sorting - priority:")
    place_collection.sort("priority")
    print(place_collection)
    # TODO: Add more sorting tests
    # Test sorting places by is_visited attribute
    print("Test sorting - is_visited:")
    place_collection.sort("is_visited")
    print(place_collection)

    # Test sorting places by country attribute
    print("Test sorting - country:")
    place_collection.sort("country")
    print(place_collection)

    # Test sorting places by name attribute
    print("Test sorting - name:")
    place_collection.sort("name")
    print(place_collection)
    # TODO: Test saving places (check CSV file manually to see results)
    # Test saving places to file
    print("Test saving places:")
    place_collection.save_places('places.csv')
    print("Save completed.")
    # TODO: Add more tests, as appropriate, for each method
    # Test getting number of unvisited places
    print("Test getting number of unvisited places:")
    assert place_collection.get_number_of_unvisited_places() == 3
    print(f"Expected number of unvisited places vs the actual output:\n"
          f"3 vs {place_collection.get_number_of_unvisited_places()}")


run_tests()
