#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Funciton to add key:value pair to a_dictionary

    Args:
        a_dictionary: Given dictionary to modify
        key: key to the new value to add to _dictionary
        value: new value to add to a_dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
