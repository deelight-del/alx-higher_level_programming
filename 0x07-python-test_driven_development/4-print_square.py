#!/usr/bin/python3
"""This module contatins the function to
print and repreesent squares with a series of
the pound/hash symbol.
"""


def print_square(size):
    """Function to print a square as given
    and annotated by the size.

    Args:
        size: The size of the square, given as only ints.

    Return:
        None. But prints output to the screen.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")

    elif size == 1:
        print("#")

    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
