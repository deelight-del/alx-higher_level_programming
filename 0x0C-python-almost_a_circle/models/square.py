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
    
    def update(self, *args, **kwargs):
        """The method that uses no-keyword and keyword
        variable length of ordered and keyed argument to update
        the attributes of a given instance of this class"""
        lst_args = ["id", "size", "x", "y"]
        if len(args) != 0:
            for i, arg in enumerate(args):
                if i < len(lst_args):
                    setattr(self, lst_args[i], arg)
        else:
            if len(kwargs) > 0:
                for key, val, in kwargs.items():
                    if key in lst_args:
                        setattr(self, key, val)

    def to_dictionary(self):
        """Public method to convert a given object to the dictionary
        representation of that object with its various attributes"""
        self.__attrdict = {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
        return self.__attrdict
