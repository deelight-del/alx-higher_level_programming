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

    def area(self):
        """method to perform calcualtion of the
        area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self, shape="Rectangle"):
        """Magic function that the str function and print
        function will make use of
        """
        return "[{:s}] {:d}/{:d}".format(shape, self.__width, self.__height)
