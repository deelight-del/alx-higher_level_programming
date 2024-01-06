#!/usr/bin/python3
"""a Python script that fetches
from the url passed to it, and POST a data sent to it
and then prints the information returned"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    r = requests.post(url, data=data)
    print(r.text)
