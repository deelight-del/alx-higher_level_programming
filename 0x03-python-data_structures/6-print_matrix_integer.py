#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    lent = len(matrix)
    for i in range(lent):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end=" ")
        print()

