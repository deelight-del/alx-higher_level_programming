#!/usr/bin/python3
"""This module contains the class definiton of the
Base class that our future classes will be inheriting
from.
"""


class Base:
    """Class definition of Base
    """
    __nb_objects = 0

    @classmethod
    def increase_object(cls):
        cls.__nb_objects += 1
        return cls.__nb_objects

    def __init__(self, id=None):
        """Init definition of class
        """
        self.id = id

    @property
    def id(self):
        """property decorator of the attr id"""
        return self.__id

    @id.setter
    def id(self, id):
        """setter property of the attribute id"""
        if id is not None:
            self.__id = id
        else:
            Base.increase_object()
            self.__id = __nb_objects
