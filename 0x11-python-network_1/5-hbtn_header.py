#!/usr/bin/python3
"""
Module: fetch_x_request_id

Description:
This script takes in a URL, sends a request to the URL,
    and displays the value of the variable X-Request-Id
    in the response header.

Usage:
./fetch_x_request_id.py <URL>

Arguments:
- <URL>: The URL to send the request to.

Requirements:
- Uses the packages requests and sys.
- Does not import packages other than requests and sys.

Output:
- Displays the value of the variable X-Request-Id
    in the response header.
"""
import requests
import sys


if len(sys.argv) != 2:
    print("Usage: {} <URL>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)

x_request_id = response.headers.get('X-Request-Id')

if x_request_id:
    print(x_request_id)
else:
    print("X-Request-Id header not found in the response")
