#!/usr/bin/python3
"""This module contains the
class definition of the class Rectangle and
its respective methods, and attributes.
"""


class Rectangle:
    """Class definition of
    Rectangle, including methoda and attributes
    """
    def __init__(self, width=0, height=0):
        """The init mehtod of our class

        Args:
            self: reference to object instance
            width: The width dimension passed into creating the object.
            height: The height dimension passed into creating the object.

        Return:
            None.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property of the width object to get the width
        object respectively.
        """
        return self.__width

    @width.setter
    def width(self, w):
        """The accompanying setter function of the property
        width above.
        """
        if type(w) is not int:
            raise TypeError("width must be an integer")
        elif w < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = w

    @property
    def height(self):
        """property getter method for
        reading the height dimension
        """
        return self.__height

    @height.setter
    def height(self, h):
        """setter for the heighr parameter
        or height dimension
        """
        if type(h) is not int:
            raise TypeError("height must be an integer")
        elif h < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = h
