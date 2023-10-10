#!/usr/bin/pyhton3

"""This module contain function defintions that help return a
list of lists that reperesents the pascal triangle
"""


def next_triangle(prev_list):
    """Function that takes the previous list and outputs the
    ncxt list of the pascal triangle

    Args:
        prev_list: prev_list to generate the next triangle.

    Return:
        None
    """
    next_list = [1]
    prev = prev_list[0]
    for ele in prev_list[1:]:
        result = ele + prev
        next_list.append(result)
        prev = ele
    next_list.append(1)
    return next_list


def pascal_triangle(n):
    """This is the function that returns a pascal triangle
    according to n that is passed into the function

    Args:
        prev_list: prev_list to generate the next triangle.

    Return:
        None
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    list_of_lists = [[1], [1, 1]]
    n_iter = n - 2
    for i in range(n_iter):
        result = next_triangle(list_of_lists[-1])
        list_of_lists.append(result)
    return list_of_lists
