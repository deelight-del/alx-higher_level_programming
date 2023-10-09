#!/usr/bin/python3
"""This module contains the function
definition of the inherits_form function that
checks if an object obj is of class a_class that inherits
directly or indirectly from a_class.
"""


def inherits_from(obj, a_class):
    """This function checks if the object obj is
    inherits (i.e. subclass) of a_class directly or indirectly

    Args:
        obj: object to test.
        a_class: the class to check object for.

    Returns:
        True or False.
    """

    if (obj.__class__ == a_class):
        return False
    if issubclass(obj.__class__, a_class):
        return True
    else:
        return False
