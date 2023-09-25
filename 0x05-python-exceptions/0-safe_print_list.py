#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Function to safe_print the elements in a list and return the
    number of printed elements

    Args:
        my_list: A given list that is passed into the funciton
        x: Supposed extent to print the list.

    Return:
        An integer that reperesents the number of actual elements printed
    """

    if isinstance(my_list, list):
        for i in range(0, x):
            try:
                print(my_list[i], end="")
            except IndexError as e:
                print()
                if i <= 0:
                    return 0
                return i
        print()
        return (i + 1)
    else:
        return 0
