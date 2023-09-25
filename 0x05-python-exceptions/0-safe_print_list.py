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
        count = 0
        try:
            for val in my_list:
                print(val, end="")
                count = count + 1
            print()
        except IndexError as e:
            print()
        return (count)
    else:
        return 0
