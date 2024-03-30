#!/usr/bin/python3
"""
Module: fetch_github_id

Description:
This script takes GitHub credentials (username and personal access token)
    and uses the GitHub API to display the user's id.
It uses Basic Authentication with the provided username and
    personal access token to access the user's information.

Usage:
./fetch_github_id.py <username> <personal_access_token>

Arguments:
- <username>: Your GitHub username.
- <personal_access_token>: Your GitHub personal access token.

Requirements:
- Uses the packages requests and sys.
- Does not import packages other than requests and sys.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        print("{}".format(user_data['id']))
    else:
        print("None")
