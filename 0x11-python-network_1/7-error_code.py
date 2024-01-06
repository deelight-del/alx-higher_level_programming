#!/usr/bin/python3
""" A Python script that takes in a URL,
sends a request to the URL and displays the
body of the response.."""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print("Error code:", r.status_code)
