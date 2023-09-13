#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Function to delete a respective value from a dictionary with 
    respective key

    Args:
        a_dictionary: A dictionary to modify
        key: A string, which function uses to modify a_dictionary,
        if it can't be found, nothing happens.
    """
    if (a_dictionary.get(key, None) is None):
        return a_dictionary
    del a_dictionary[key]
    return a_dictionary
