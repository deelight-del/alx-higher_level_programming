#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Multiply each value in a_dictionary by 2 and return the new dictionary

    Args:
        a_dictionary: dictionary to multiply respective values by 2.

    Returns:
        A new dictionary with the values of a_dictionary multiplies by 2
    """
    new_dictionary = {}
    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2
    return new_dictionary
