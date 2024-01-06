#!/usr/bin/python3
"""a Python script that fetches
information about a given URL on the command line interface
This script retrieves the header value of a particular value"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as r:
        headers = r.headers
        print(headers.get("X-Request-Id"))
