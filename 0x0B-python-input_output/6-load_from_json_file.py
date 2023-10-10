#!/usr/bin/python3
"""This module contains the function defintion of load_from_json_file
that returns a python object from a json string stored in a json file
"""


import json


def load_from_json_file(filename):
    """Function that returns a python object from a
    json string stored in a json file.

    Args:
        filename: filename of the json file to load from.

    Return:
        None
    """
    with open(filename, mode="r") as f:
        return json.load(f)
