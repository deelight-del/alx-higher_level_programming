#!/usr/bin/python3
"""This contains listing the commits
of rails repo by rails user"""


if __name__ == "__main__":
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]
    headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            }
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url, headers)
    try:
        json_data = response.json()
        for eachCommit in json_data[0:10]:
            print(
                    eachCommit.get("commit").get("tree").get("sha") + ": " +
                    eachCommit.get("commit").get("committer").get("name")
                    )
    except (
            requests.exceptions.JSONDecodeError,
            requests.exceptions.HTTPError
            ):
        pass
