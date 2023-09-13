#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Function to add all integers in a list only one.
    Skip a given constant integer that has been added before.

    Args:
        my_list: The list to perform unique additon upon.

    Returns:
        Returns a given value as the result of the unique additon
    """
    if isinstance(my_list, list):
        return sum(list(set(my_list)))
