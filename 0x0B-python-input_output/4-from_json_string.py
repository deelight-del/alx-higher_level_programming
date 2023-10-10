#!/usr/bin/python3
"""Module containing the function defintion of
from_json_string, that converts a json string to a python object
"""

import json


def from_json_string(my_str):
    """Function to convert my_str to a python object.

    Args
        my_obj: A typical python object.

    Return:
        A Json string/objeect
    """
    return json.loads(my_str)
