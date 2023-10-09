#!/usr/bin/python3
"""This module contains the class defintion of
MyList that inherits from the class `list` and
then contains the public method to sort the list
"""


class MyList(list):
    """The class definition of MyList
    that inherits from list class
    """

    def print_sorted(self):
        """Public method that sorts the given
        list object.
        """
        self.sort()
        print(self)
        return self
