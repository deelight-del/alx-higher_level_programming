#!/usr/bin/python3
"""This module contains the function definition of the
add_attribute tha sets an attribut if it can and raises
a type error when it cannot.
"""


def add_attribute(obj, name, attr):
    """Function that adds a new attribute to
    an object if it can and raises a typeerror if it cannot.

    Args:
        obj: object to add attr to.
        name: name of attribute.
        attr: value of attr

    Return:
        None.
    """

    if hasattr(obj, '__dict__'):
        setattr(obj, name, attr)
    else:
        raise TypeError("can't add new attribute")
