#!/usr/bin/python3
"""a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""


if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    payload = dict()
    try:
        payload['q'] = sys.argv[1]
    except IndexError:
        payload['q'] = ""
    response = requests.post(url, data=payload)
    try:
        response.raise_for_status()
        json_format_data = response.json()
        if not json_format_data:
            print("No result")
        else:
            result = (
                    "[" + str(json_format_data['id']) + "] " +
                    json_format_data['name']
                    )
            print(result)
    except (
            requests.exceptions.JSONDecodeError,
            requests.exceptions.HTTPError,
            ):
        if int(respons.status_code) == 204:
            print("No result")
        else:
            print("Not a valid JSON")
