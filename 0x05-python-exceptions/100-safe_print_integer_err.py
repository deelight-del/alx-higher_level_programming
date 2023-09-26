#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Function to safe print an integer or error to stderr

    Args:
        value: The given integer to print.

    Return:
        True or False. Depending on behaviour of program
    """

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        sys.stderr.write("Exception: ")
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        return False
