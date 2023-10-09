#!/usr/bin/python3
"""This module contains the class definition of Rectangle that contains
particular attributes and methods for different functionsonalities.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class defintion of the Rectangle
    geometry.
    """

    def __init__(self, width, height):
        """The init magic method initializer for object rectangle.
        It inherits from the BaseGeometry class
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
