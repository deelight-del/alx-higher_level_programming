#!/usr/bin/python3
"""a Python script that fetches
https://alx-intranet.hbtn.io/status and returns
meaningful information about it using requests module"""

if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    content = r.text
    type_content = type(content)
    result = (
            'Body response:\n'
            f'\t- type: {type_content}\n'
            f'\t- content: {content}'
            )
    print(result)
