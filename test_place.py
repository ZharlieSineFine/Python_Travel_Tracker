"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    # TODO: Write tests to show this initialisation works
    assert new_place.name == "Malagar"
    assert new_place.country == "Spain"
    assert new_place.priority == 1
    assert not new_place.is_visited
    print(f"Expected string form of new_place vs actual output:\n"
          f"Malagar in Spain, priority 1, visited or not: False.\n{new_place}")
    # TODO: Add more tests, as appropriate, for each method
    # Test mark_as_visited method
    print("Test mark_as_visited method:")
    new_place.mark_as_visited()  # Change is_visited of new_place to True
    assert new_place.is_visited
    print(f"Expected string form of new_place vs actual output:\n"
          f"Malagar in Spain, priority 1, visited or not: True.\n{new_place}")

    # Test mark_as_unvisited method
    print("Test mark_as_unvisited method:")
    new_place.mark_as_unvisited()  # Change is_visited of new_place to False
    assert not new_place.is_visited
    print(f"Expected string form of new_place vs actual output:\n"
          f"Malagar in Spain, priority 1, visited or not: False.\n{new_place}")

    # Test is_important method
    print("Test is_important method:")
    assert new_place.is_important()
    print(f"Expected value of new_place.is_important() vs actual output:\nTrue\n{new_place.is_important()}")

    another_place = Place("Qingdao", "China", 3, False)
    assert not another_place.is_important()
    print(f"Expected value of another_place.is_important() vs actual output:\nFalse\n{another_place.is_important()}")


run_tests()
