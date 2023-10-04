#!/usr/bin/python3

"""When testing or dealing with operations where
their value change from time to time, e.g. local time
current date, object ids (since they will be loaded into 
different portion of memories at different time, e.t.c
We can use the ellipsis to match part of the substring that 
does change regularly. Especially, when such substring do not
really matter in making an effective test
"""

class MyClass:
    pass

def unpredictable(obj):
    """Return a list of MyClass Objext.

    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<using_elipsis.MyClass object at 0x...>]
    """
    return [obj]

