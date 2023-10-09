#!/usr/bin/python3
"""This module contains the class definition of Rectangle that contains
particular attributes and methods for different functionsonalities.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class defintion of the Square
    geometry.
    """

    def __init__(self, size):
        """The init magic method initializer for object square.
        It inherits from the Rectangle class
        """
        Rectangle.integer_validator(self, "size", size)
        self.__size = size
        Rectangle.__init__(self, self.__size, self.__size)

    def area(self):
        """method to perform calcualtion of the
        area of the square
        """
        return self.__size * self.__size

    def __str__(self, shape="Square"):
        return super().__str__(shape)
