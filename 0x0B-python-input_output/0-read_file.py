#!/usr/bin/python3
"""This module contains the
function definition of the read_file
function that simply reads a file and prints out the content
"""


def read_file(filename=""):
    """Funciton defintion of read_file that reads a file
    adn prints out its content.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        content = f.read()
    print(content, end="")
