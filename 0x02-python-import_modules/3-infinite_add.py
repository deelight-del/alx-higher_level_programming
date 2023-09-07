#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    result = 0
    if len(argv) <= 1:
        print("{:d}".format(0))
    else:
        for arg in argv[1:]:
            result = result + int(arg)
        print("{:d}".format(result))
