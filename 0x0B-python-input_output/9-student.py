#!/usr/bin/python3
"""This module contains the class definition of Student
that conatins different attributes and methods.
"""


class Student:
    """The defintion of the Student class with multiple
    methods and attributes alike
    """
    def __init__(self, first_name, last_name, age):
        """Defining the init method of the class to first_name,
        last_name, and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This reterives the dictionary reperesentation of the class
        instance
        """
        return self.__dict__
