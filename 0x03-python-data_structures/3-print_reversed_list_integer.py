#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        lent = len(my_list)
        i = lent - 1
        while i >= 0:
            print("{:d}".format(my_list[i]))
            i -= 1
