#!/usr/bin/python3

def print_reversed_list_integer(my_list[]):
    lent = len(my_list)
    if lent <= 0:
        pass
    else:
        i = lent - 1
        while i >= 0:
            print("{:d}".format(my_list[i]))
