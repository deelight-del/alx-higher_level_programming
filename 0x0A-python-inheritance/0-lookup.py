#!/usr/bin/python3
"""This module contains the function definition
to list all the attributes and methods of an object
"""


def lookup(obj):
    """Function definition that lists the
    attributes and methods of a given object

    Args:
        obj: The object passed into the function

    Return:
        returns a list of attributes and methods of obj.

    """

    return dir(obj)
