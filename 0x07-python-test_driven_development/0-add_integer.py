#!/usr/bin/python3

"""This module contains the function
definition of the addition of two intgers.
Where floats are casted to integers.
"""


def add_integer(a, b=98):
    """Integer addition of two numbers.

    Args:
        a: The first operand.
        b: The second operand.

    Return:
        The return value is an intger, provided it is an int or float.
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
