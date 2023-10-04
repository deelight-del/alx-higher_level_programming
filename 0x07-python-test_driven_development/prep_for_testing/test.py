#!/usr/bin/python3

import doctest

def my_function(x, y):
    """
    Returns the sum of x and y.

    >>> my_function(2, 3) #doctest: +REPORT_UDIFF
    4

    >>> my_function(2, -3) #doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE, +REPORT_CDIFF
    -2
    """
    return x + y

if __name__ == "__main__":
    doctest.testmod()
