#!/usr/bin/python3
"""This module contains the function definition of class_
to_json that returns the dictionary reperesentation of the
given object
"""


def class_to_json(obj):
    """Function to return the dictionary reperesntation
    of object obj
    """
    return obj.__dict__
