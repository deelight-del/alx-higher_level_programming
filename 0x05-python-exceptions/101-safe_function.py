#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """Function to peforma a function <fct> in a safe manner

    Args:
        fct: A funciton pointer that accepts arguments
        args: Arguments that are passed int the fct function pointer

    Return:
        Returns the given value of the function or otherwise
    """

    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
