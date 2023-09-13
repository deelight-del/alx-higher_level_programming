#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Function to search and replace a given element in a list.

    Args:
        my_list: Original list to replace.
        search: The element to search for in the list
        replace: Element to replace the search

    Returns:
        A new list that will have element search replaced by
        element replace.
    """
    if isinstance(my_list, list):
        return list(map(lambda x: replace if x == search else x, my_list))
