#!/usr/bin/python3

def safe_print_integer(value):
    """Function to safe print an integer

    Args:
        value: The given integer to print.

    Return:
        True or False. Depending on behaviour of program
    """

    try:
        x = int(value)
        print("{:d}".format(x))
        return True
    except ValueError:
        return False
