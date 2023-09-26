#!/usr/bin/python3

"""This file is going to contain the class definition of
Square and its respective attributes
This is module that will contain the class defintion of the
Square class for creatting classes.
"""


class Square:
    """Square A class that abstracts the data
    square.

    Takes no attribute for now.

    It also does not return anything or take any method
    """
    def __init__(self, size=0):
        """Method to initialize the size of
        a square

        Args:
            self: Object reference to itself
            size: size of the square.

        Return:
            Nothing
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Function to calculate the area of a square
        given the size

        Args:
            self: The instance of this class

        Return:
            An integer value. The area of the square.
        """
        return (self.__size ** 2)
