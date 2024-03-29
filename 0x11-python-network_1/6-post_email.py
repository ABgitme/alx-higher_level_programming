#!/usr/bin/python3
"""
Module: send_post_request

Description:
This script takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response.

Usage:
./send_post_request.py <URL> <email>

Arguments:
- <URL>: The URL to send the POST request to.
- <email>: The email address to be sent as a
parameter in the POST request.

Requirements:
- Uses the packages requests and sys.
- Does not import packages other than requests and sys.

Output:
- Displays the body of the response.
"""
import requests
import sys


url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}
response = requests.post(url, data=data)

print(response.text)
