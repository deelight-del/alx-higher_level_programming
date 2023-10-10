#!/usr/bin/python3
"""This module contains the function defintion of save_to_json_file
that stores a python object inside a json file as json string.
"""


import json


def save_to_json_file(my_obj, filename):
    """Function that saves my_obj into filename as json
    string that can be loaded later on.

    Args:
        my_obb: The object to load
        filename: filename of the json file to load it into.

    Return:
        None
    """
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
