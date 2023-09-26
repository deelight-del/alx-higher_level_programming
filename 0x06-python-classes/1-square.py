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
    def __init__(self, size):
        """Method to initialize the size of
        a square

        Args:
            self: Object reference to itself
            size: size of the square.

        Return:
            Nothing
        """
        self.__size = size
