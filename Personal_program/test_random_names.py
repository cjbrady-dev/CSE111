import pytest
from pytest import *
from random_names import *

lt_one = ["John Doe","Jane Doe","Boby Bill","Jonny Little","Napolion Bonapart","Jan Truly"]
lt_two = ["1 + 1","1 + 2","1 + 3","1 + 4","1 + 5","1 + 6","1 + 7","1 + 8","1 + 9","1 + 10"]


def main():
    test_student_name()

    pass

def test_student_name():
    """ Verify that student_name is generating a random name from the Names.CSV print to GUI 
    Paramaters:csv_file_names
    Return: return chosen_row[0]
    """

    assert student_name(csv_file_names) in lt_one

def test_expression():
    """ Verify that student_name is generating a random exprestion from the Expression.CSV print to GUI
    Paramaters:csv_file_expressions
    Return: return chosen_row[0]
    """
    assert expression(csv_file_expressions) in lt_two


pytest.main(["-v", "--tb=line", "-rN", __file__])