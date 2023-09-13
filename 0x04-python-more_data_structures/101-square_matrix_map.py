#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x: [ele * ele for ele in x], matrix))
