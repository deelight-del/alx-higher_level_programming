#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Function to safe print integers only in a list.

    Args:
        my_list: The list of values to print from
        x: Initialized to zero. The extent to print from

    Return:
        The real number of elements printed from my_list.
    """

    if isinstance(my_list, list):
        if (x <= 0):
            return (0)
        i = j = 0
        while (j < x):
            try:
                print("{:d}".format(my_list[j]), end="")
                i = i + 1
            except (ValueError, TypeError):
                pass
            j = j + 1
        print()
        return i
    else:
        return (0)
