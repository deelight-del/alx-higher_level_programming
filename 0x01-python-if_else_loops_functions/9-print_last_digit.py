#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        # make number positive if < 0
        holder = number * -1
        # obtain the last and make it negative
        last = (holder % 10)
    else:
        last = number % 10
    print("{:d}".format(last), end="")
    return last
