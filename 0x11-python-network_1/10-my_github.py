#!/usr/bin/python3
"""This file contains using GH username and
personal access tokens to access user informations"""


if __name__ == "__main__":
    import sys
    import requests

    username = sys.argv[1]
    token = sys.argv[2]
    header_dictionary = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28"
            }
    user_url = f"https://api.github.com/{username}"
    response = requests.get(user_url, headers=header_dictionary)
    json_result = response.json()
    print(json_result.get('id'))
