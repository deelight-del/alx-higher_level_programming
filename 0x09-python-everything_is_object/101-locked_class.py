#!/usr/bin/python3
"""htis module contains the class definition
of LockedClass that uses the __slot__ magic
"""


class LockedClass:
    """This is the class definition of LockedClass
    that accepts only one attribute for interaction.
    """

    __slots__ = ["first_name"]
