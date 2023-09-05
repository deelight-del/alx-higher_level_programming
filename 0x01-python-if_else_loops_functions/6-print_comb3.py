#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 10):
        if (j > i):
            print("{0:d}{1:d}".format(i, j), end="")
            if (i == 8 and j == 9):
                print("\n", end="")
            else:
                print(", ", end="")
