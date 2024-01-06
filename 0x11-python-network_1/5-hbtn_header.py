#!/usr/bin/python3
"""a Python script that fetches
https://alx-intranet.hbtn.io and returns
meaningful information about it using requests module"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
