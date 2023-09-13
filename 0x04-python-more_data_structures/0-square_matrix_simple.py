#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Function to square values in a matrix

    Args:
        matrix: List of lists to square

    Returns:
        Returns a list of list that is squared and
        different from inpur list.
    """
    if isinstance(matrix, list):
        new_matrix = []
        for _list in matrix:
            new_matrix.append(list(map(lambda x: x*x, _list)))
        return new_matrix
