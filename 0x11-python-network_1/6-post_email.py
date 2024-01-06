#!/usr/bin/python3
"""a Python script that fetches
from the url passed to it, and POST a data sent to it"""

if __name__ == "__main__":
    import requests
    import sys
    req = requests.post(sys.argv[1], data={'email': sys.argv[2])
    print(req.text)
