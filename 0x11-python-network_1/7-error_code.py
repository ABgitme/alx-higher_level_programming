#!/usr/bin/python3
"""
Module: fetch_url_response

Description:
This script takes in a URL, sends a request to the URL,
    and displays the body of the response.
If the HTTP status code is greater than or equal to 400,
    it prints "Error code:" followed by the value of the HTTP status code.

Usage:
./fetch_url_response.py <URL>

Arguments:
- <URL>: The URL to send the request to.

Requirements:
- Uses the packages requests and sys.
- Does not import packages other than requests and sys.

Output:
- Displays the body of the response.
- Prints "Error code:" followed by the value of the HTTP
    status code if the status code is greater than or equal to 400.
"""
import requests
import sys


url = sys.argv[1]

response = requests.get(url)

if response.status_code >= 400:
    print("Error code:", response.status_code)
else:
    print(response.text)
