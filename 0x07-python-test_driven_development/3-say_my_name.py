#!/usr/bin/python3
"""This module contatin function definition to
function say_my_name that prints the first and the last name
given to it.
"""


def say_my_name(first_name, last_name=""):
    """Function to print my name and last name.

    Args:
        first_name: fist nmae to print
        last_name: last name of user

    Return:
        None. But printss to stdout
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
