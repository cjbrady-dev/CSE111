# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

from chemistry import make_periodic_table
from pytest import approx
import pytest


# These are the indexes of the
# elements in the periodic table.
SYMBOL_INDEX = 0
NAME_INDEX = 1
ATOMIC_MASS_INDEX = 2


def test_make_periodic_table():
    """Verify that the make_periodic_table function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the make_periodic_table and store the returned
    # periodic table in a variable named periodic_table_list.
    periodic_table_list = make_periodic_table()
    assert isinstance(periodic_table_list, list), \
        "make_periodic_table function must return a list:" \
        f" expected a list but found a {type(periodic_table_list)}"

    # Create a key function that will be used by the sorted method.
    by_name = lambda element: element[NAME_INDEX]

    # Sort the periodic table by the element names.
    periodic_table_list = sorted(periodic_table_list, key=by_name)

    # Check each element in the sorted periodic table.
    i = 0
    check_element(periodic_table_list[i], ['Ac', 'Actinium', 227])
    i += 1
    check_element(periodic_table_list[i], ['Al', 'Aluminum', 26.9815386])
    i += 1
    check_element(periodic_table_list[i], ['Ag', 'Silver', 107.8682])
    i += 1



def check_element(actual, expected):
    """Verify that the actual element that came from the
    periodic_table_list contains the same values as the
    expected element.

    Parameters
        actual: a list that came from the periodic_table_list.
        expected: a list that contains the expected values.
    Return: nothing
    """
    name = expected[NAME_INDEX]
    assert actual[NAME_INDEX] == name, \
         f"{name} is missing from the periodic table."

    # Verify that the element's symbol is correct.
    act_symbol = actual[SYMBOL_INDEX]
    exp_symbol = expected[SYMBOL_INDEX]
    assert act_symbol == exp_symbol, \
         f"wrong symbol for {name}: " \
         f"expected {exp_symbol} but found {act_symbol}."

    # Verify that the element's atomic mass is correct.
    act_mass = actual[ATOMIC_MASS_INDEX]
    exp_mass = expected[ATOMIC_MASS_INDEX]
    assert act_mass == approx(exp_mass), \
            f"wrong atomic mass for {name}: " \
            f"expected {exp_mass} but found {act_mass}"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
