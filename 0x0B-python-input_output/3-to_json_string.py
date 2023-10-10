#!/usr/bin/python3
"""Module containing the function defintion of
to_json_string, that converts a python object to a json
string
"""

import json


def to_json_string(my_obj):
    """Function to convert my_obj to a json string.

    Args
        my_obj: A typical python object.

    Return:
        A Json string/objeect
    """
    return json.dumps(my_obj)
