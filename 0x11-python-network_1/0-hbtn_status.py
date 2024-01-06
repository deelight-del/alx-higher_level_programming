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
        print(f"\t-type: {type_content}")
        print(f"\t-content: {content}")
        print(f"\t-utf8 content: {utf_content}")
