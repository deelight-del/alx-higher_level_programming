#!/usr/bin/python3

"""A Python script that fetches
from the url passed to it, and POST a data sent to it"""

import requests
import sys

if __name__ == "__main__":
    req = requests.post(sys.argv[1], data={'email': sys.argv[2]})
