#!/usr/bin/python3
"""This module contains the
function definition of the append_write
function that simply appends into a file and returns the amount of characters
written to the file
"""


def append_write(filename="", text=""):
    """Funciton defintion of append_write that writes into a file
    adn prints out its content.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        noOfChars = f.write(text)
    return noOfChars
