#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """Function to delete a respective value from a dictionary with
    respective value. All keys with given value should be deleted.

    Args:
        a_dictionary: A dictionary to modify
        value: A given value of different types. Used to delete members of
        a_dictionary, if it can't be found, nothing happens.
    """
    keys_to_delete = []
    for k, v in a_dictionary.items():
        if v == value:
            keys_to_delete.append(k)
    for k in keys_to_delete:
        del (a_dictionary[k])
    return a_dictionary
