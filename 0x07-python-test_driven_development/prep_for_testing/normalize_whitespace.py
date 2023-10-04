#!/usr/bin/python3

import doctest

"""The Normalize whitespace optionflag/directive is used to 
match any sequence of space between the actual and expected out-
put. However, if there is no space in the actual output and there appears
space in the expected output or vice-versa, the test case would still 
fail, regardless
"""

def my_function(a, b):
    """This function multiplies any datatype a by b.

    >>> my_function(['A', 'B'], 3) #doctest: +NORMALIZE_WHITESPACE
    ['A', 'B',
    'A', 'B',
    'A', 'B']

    This below will fail because the expected output con-
    tain extra space before and after the square brackets.

    >>> my_function(['A', 'B'], 3)  #doctest: +NORMALIZE_WHITESPACE, +REPORT_NDIFF
    [ 'A', 'B',
    'A', 'B',
    'A', 'B' ]

    """

    return a * b

if __name__ == "__main__":
    doctest.testmod(verbose=True)
