#!/usr/bin/python3

"""The module that deals with log parsing as inputs of
certain characteristics
"""

import sys


if __name__ == "__main__":
    logs = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
            404: 0, 405: 0, 500: 0}
    file_size = 0
    epoch = 0

    try:
        for line in sys.stdin:
            epoch = epoch + 1
            line_list = line.split()
            file_size += int(line_list[-1])
            logs[int(line_list[-2])] += 1
            if epoch % 10 == 0:
                print("File size: {:d}".format(file_size))
                for key in logs:
                    if logs[key] > 0:
                        print("{}: {}".format(key, logs[key]))
    except (KeyboardInterrupt):
        print("File size: {:d}".format(file_size))
        for key in logs:
            if logs[key] > 0:
                print("{}: {}".format(key, logs[key]))
