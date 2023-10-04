#!/usr/bin/python3
"""This module contains the comprehensive module
for the definition of the matrix dvision of by a number
div"
"""


def matrix_divided(matrix, div):
    """matrix is a list of lists. It will contain
    only numbers. Otherwise, throws error. This function
    divides the entire matrix with a value, called div.

    Args:
        matrix: list of lists that contains only number.
        div: Number that is non zero
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
    for i, ls in enumerate(matrix):
        if type(ls) is not list:
            raise TypeError("matrix must be a matrix\
                    (list of lists) of integers/floats")
        for val in ls:
            if type(val) is not int and type(val) is not float:
                raise TypeError("matrix must be a\
                        matrix (list of lists) of integers/floats")
        if i == 0:
            size = len(ls)
            if size == 0:
                raise TypeError("matrix must be a matrix\
                        (list of lists) of integers/floats")
        else:
            if (size != len(ls)):
                raise TypeError("Each row of the matrix \
                        must have the same size")
    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    new_matrix = ([list(map(lambda x: round(x/div, 2), ls)) for ls in matrix])
    return new_matrix
