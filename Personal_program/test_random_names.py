import pytest
import random_names


def test_student_name():
    """ Verify that student_name is generating a random name from the Names.CSV print to GUI 
    Paramaters:csv_file_names
    Return: return chosen_row[0]
    """"
    names_1 = random_names(csv_file_names)
    names_2 = random_names(csv_file_names)
    assert names_1 =




def test_expression():
    """ Verify that student_name is generating a random exprestion from the Expression.CSV print to GUI
    Paramaters:csv_file_expressions
    Return: return chosen_row[0]
    """"

def test_on_button_click():
    """Verify that on_button_click generates the returned random rows of functions expression and student_name.
    Paramaters: None
    Return: student_name chosen_row[0],  expression return chosen_row[0]"""
