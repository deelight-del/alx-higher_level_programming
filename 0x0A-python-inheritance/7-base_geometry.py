#!/usr/bin/python3
"""This module contains the class definition
of BaseGeometry that contains certain attributes and
methods for certain functionalities.
"""


class BaseGeometry:
    """BaseGeometry is a class that inherits directly from
    object (Python 3.x synatx) and will contain attributes
    and methods to do stuffs.
    """
    def area(self):
        """Raises Exception

        Args:
            self: object reference.

        Return:
            None for now.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates that value is an integer
        and is > 0

        Args
            self: object referencte to instantiated objects.
            name: The name of value that we are validating.
            value: value that we are validating.

        Return:
            None if valid, raises error if not.
        """

        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
