#!/usr/bin/python3
"""a Python script that fetches
information about a given URL on the command line interface
This script must handle the HTTP error and prints the result as
utf-8 decoded"""

if __name__ == "__main__":

    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    import sys

    try:
        url = sys.argv[1]
        req = Request(url)
        with urlopen(req) as r:
            print(r.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.code)
