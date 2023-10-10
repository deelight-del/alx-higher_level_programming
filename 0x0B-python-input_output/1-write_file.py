#!/usr/bin/python3
"""This module contains the
function definition of the write_file
function that simply write into a file and returns the amount of characters
written to the file
"""


def write_file(filename="", text=""):
    """Funciton defintion of write_file that writes into a file
    adn prints out its content.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        noOfChars = f.write(text)
    return noOfChars
