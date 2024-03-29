#!/usr/bin/python3
"""
Module: fetch_recent_commits

Description:
This script fetches the 10 most recent commits
    of a repository from GitHub by the specified owner and repository name.
It then prints each commit in the format: <sha>: <author name>

Usage:
./fetch_recent_commits.py <repository_name> <owner_name>

Arguments:
- <repository_name>: The name of the repository.
- <owner_name>: The name of the repository owner.

Requirements:
- Uses the packages requests and sys.
- Does not import packages other than requests and sys.
"""
import requests
import sys


if len(sys.argv) != 3:
    sys.exit(1)

repository_name = sys.argv[1]
owner_name = sys.argv[2]
url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

response = requests.get(url)

if response.status_code == 200:
    commits = response.json()[:10]  # Get the 10 most recent commits
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
else:
    print("Error accessing GitHub API. Status code:", response.status_code)
