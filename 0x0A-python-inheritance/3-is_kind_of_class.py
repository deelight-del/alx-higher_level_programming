#!/usr/bin/python3
"""This module contains the function
definition of the is_same_class function that
checks if an object obj is of class a_class/ class
that inherits from a_class.
"""


def is_kind_of_class(obj, a_class):
    """This function checks if the object obj is
    an instance of the class a_class or a class thata inherits
    from a_class

    Args:
        obj: object to test.
        a_class: the class to check object for.

    Returns:
        True or False.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
