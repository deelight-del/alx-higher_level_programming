#!/usr/bin/python3
"""a Python script that fetches
from the url passed to it, and POST a data sent to it
and then prints the information returned"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    mail = sys.argv[2]
    payload = {"email": mail}
    r = requests.post(url, data=payload)
    print(r.text)
