#!/usr/bin/python3
"""
Module: fetch_url_response

Description:
This script takes in a URL, sends a request to the URL,
    and displays the body of the response (decoded in utf-8).
It manages urllib.error.HTTPError exceptions and prints
    "Error code:" followed by the HTTP status code.

Usage:
./fetch_url_response.py <URL>

Arguments:
- <URL>: The URL to send the request to.

Requirements:
- Uses the packages urllib and sys.
- Does not import packages other than urllib and sys.
- Uses the with statement.

Output:
- Displays the body of the response (decoded in utf-8)
    if the request is successful.
- Prints "Error code:" followed by the HTTP
status code if an HTTPError occurs.

Example:
./fetch_url_response.py https://example.com
"""
import urllib.request
import urllib.error
import sys


if len(sys.argv) != 2:
    print("Usage: {} <URL>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
