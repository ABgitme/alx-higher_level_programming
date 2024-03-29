#!/usr/bin/python3
"""
Module: send_post_request

Description:
This script takes in a URL and an email,
sends a POST request to the URL with the email as a parameter,
and displays the body of the response (decoded in utf-8).

Usage:
./send_post_request.py <URL> <email>

Arguments:
- <URL>: The URL to send the POST request to.
- <email>: The email to be sent as a
parameter in the POST request.

Requirements:
- Uses the packages urllib and sys.
- Does not import packages other than urllib and sys.
- Uses the with statement.

Output:
- Displays the body of the response (decoded in utf-8).

Example:
./send_post_request.py https://example.com test@example.com
"""
import urllib.request
import urllib.parse
import sys


if len(sys.argv) != 3:
    print("Usage: {} <URL> <email>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')
req = urllib.request.Request(url, data=data, method='POST')

try:
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.URLError as e:
    print("Error: Failed to fetch URL -", e)
