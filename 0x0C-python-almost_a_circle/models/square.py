#!/usr/bin/python3
"""This module contains the class defintion of the class
called Square. This class consists of different methods
and attributes that are particular to the Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the data encapsulation of the Square
    class that represents a typical Square. It will
    inherit from the Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """The init method of the Square class construction"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The __str__ magic method that is used to print the class
        instances"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
            self.width))

    @property
    def size(self):
        """The property for returning the size attribute"""
        return self.width

    @size.setter
    def size(self, size):
        """setter method for the size attribute"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = self.height = size
