#!/usr/bin/python3
"""This module contains the function definition of append_after
that appends a new string after a line of string
"""


def append_after(filename="", search_string="", new_string=""):
    """The function to append a new line of text new_string
    to a an already existing file text filename
    """
    with open(filename, mode="r+", encoding='utf-8') as f:
        lines = f.readlines()
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)
        f.seek(0)
        f.truncate()
        f.writelines(new_lines)
