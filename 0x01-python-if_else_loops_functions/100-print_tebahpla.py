#!/usr/bin/python3

for i in range(122, 96, -1):
    if i % 2 == 1:
        char = chr(i - 32)
    else:
        char = chr(i)
    print("{:s}".format(char), end="")
