#!/usr/bin/python3
"""
Module: fetch_x_request_id

Description:
This script takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable
found in the header of the response.

Usage:
./fetch_x_request_id.py <URL>

Arguments:
- <URL>: The URL to send the request to.

Requirements:
- Uses the packages urllib and sys.
- Does not import packages other than urllib and sys.
- The value of the X-Request-Id variable is
different for each request.
- Does not need to check arguments passed
to the script (number or type).
- Uses a with statement.

Output:
- The value of the X-Request-Id variable found in the
header of the response, or a message indicating that
the header was not found.
- Error message if the request fails.

Example:
./fetch_x_request_id.py https://example.com
"""
import urllib.request
import sys


if len(sys.argv) != 2:
    print("Usage: {} <URL>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response")
except urllib.error.URLError as e:
    print("Error: Failed to fetch URL -", e)
