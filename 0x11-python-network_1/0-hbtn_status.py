#!/usr/bin/python3
"""a Python script that fetches
https://alx-intranet.hbtn.io/status and returns
meaningful information about it using urlib.requests"""

if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as r:
        content = r.read()
        utf_content = content.decode('utf-8')
        type_content = type(content)
        print("Body response:")
        print("\t-type: {}".format(type_content))
        print("\t-content: {}".format(content))
        print("\t-utf8 content: {}".format(utf_content))
