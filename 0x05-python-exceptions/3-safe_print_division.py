#!/usr/bin/python3

def safe_print_division(a, b):
    """Funciton to print safe division

    Args:
        a: first operand
        b: second opearand.

    Return:
        A value or some integer
    """

    try:
        c = a/b
    except ZeroDivisionError as e:
        c = None
    finally:
        print("Inside result: {}".format(c))
        return c
