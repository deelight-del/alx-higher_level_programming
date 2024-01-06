#!/usr/bin/python3
"""a Python script that fetches
from the url passed to it, and POST a data sent to it
and then prints the information returned using the text attr"""

if __name__ == "__main__":
    import requests
    import sys
    req = requests.post(sys.argv[1], data={'email': sys.argv[2])
    print(req.text)
