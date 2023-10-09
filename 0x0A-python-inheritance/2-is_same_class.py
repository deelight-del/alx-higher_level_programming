#!/usr/bin/python3
"""This module contains the function
definition of the is_same_class function that
checks if an object obj is of class a_class.
"""


def is_same_class(obj, a_class):
    """This function checks if the object obj is
    EXACTLY of the class a_class.

    Args:
        obj: object to test.
        a_class: the class to check object for.

    Returns:
        True or False.
    """

    if type(obj) == a_class:
        return True
    else:
        return False
