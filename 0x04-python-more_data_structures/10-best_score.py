#!/usr/bin/python3

def best_score(a_dictionary):
    """Function to return key of a_dictionary with the highest value

    Args:
        a_dictionary: A dictionary with the key value pair
    Returns:
        Returns the respective key or None otherwise
    """
    if (not isinstance(a_dictionary, dict) or len(a_dictionary) == 0):
        return None
    highest = sorted(a_dictionary)[0]
    highest_value = a_dictionary[highest]
    for key, value in a_dictionary.items():
        if value > highest_value:
            highest = key
            highest_value = value

    return highest
