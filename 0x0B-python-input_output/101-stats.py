#!/usr/bin/python3

"""The module that deals with log parsing as inputs of
certain characteristics
"""

if __name__ == "__main__":
    import sys
    logs = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
            404: 0, 405: 0, 500: 0}
    file_size = 0
    epoch = 0

    try:
        for line in sys.stdin:
            epoch = epoch + 1
            line_list = line.split()
            file_size += int(line_list[-1])
            try:
                error_code = int(line_list[-2])
                if logs.get(error_code, -1) != -1:
                    logs[error_code] += 1
            except ValueError:
                pass
            if epoch % 10 == 0:
                print("File size: {}".format(file_size))
                for key in sorted(logs.keys()):
                    if logs[key] > 0:
                        print("{}: {}".format(key, logs[key]))
        else:
            print("File size: {}".format(file_size))
            for key in sorted(logs.keys()):
                if logs[key] > 0:
                    print("{}: {}".format(key, logs[key]))

    except (KeyboardInterrupt):
        print("File size: {}".format(file_size))
        for key in logs:
            if logs[key] > 0:
                print("{}: {}".format(key, logs[key]))
        raise
