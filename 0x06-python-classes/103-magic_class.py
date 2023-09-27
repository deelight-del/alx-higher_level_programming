#!/usr/bin/python3

"""This module contains implementation
of the class MagicClass that actually behavies
like a circle.
"""
import math


class MagicClass:
    """This is the class definition of the 
    MagicClass and its respective properties/behaviour/
    attribues.
    """
    def __init__(self, radius=0):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
