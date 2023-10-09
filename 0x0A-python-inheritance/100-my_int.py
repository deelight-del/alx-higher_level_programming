#!/usr/bin/python3
"""This module contains the class definition of the MyInt class
that is a rebel and reverts the equal and not equal to fuction.
"""


class MyInt(int):
    """Class defintion of MyInt Class.
    A rebel class
    """

    def __eq__(self, obj):
        """The equal to method of the
        which is a magic maethod.
        """
        return int.__ne__(self, obj)

    def __ne__(self, obj):
        """The not equal to method of the
        MyInt class that reverts the way the normal
        nethod works.
        """
        return int.__eq__(self, obj)
