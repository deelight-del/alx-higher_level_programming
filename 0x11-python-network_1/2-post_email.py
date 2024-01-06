#!/usr/bin/python3
"""a Python script that fetches
information about a given URL on the command line interface
This script POST an email up the server and returns a message in
utf-8 decoded"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    mail = sys.argv[2]
    data = {"email": mail}
    data = urllib.parse.urlencode(data).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(url, data) as r:
        print(r.read().decode('utf-8'))
