#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Function to print sorted dictionaries by keys.

    Args:
        a_dictionary: Given dictionary to function

    Returns:
        None. But prints.
    """
    for keys in sorted(a_dictionary):
        print("{:s}".format(keys), end=": ")
        print(a_dictionary[keys])
