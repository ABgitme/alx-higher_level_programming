#!/usr/bin/python3
"""
Module: 0-hbtn_status

Description:
This script fetches the status of
https://alx-intranet.hbtn.io/status using the
urllib package.
It displays information about the
response body in the specified format.

Usage:
Run the script and pipe the output to `cat -e`
to display the response body with proper formatting.

Output Format:
- Body response:
    - type: <class 'bytes'>
    - content: b'OK'
    - utf8 content: OK
"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()
    utf8_content = body.decode('utf-8')

print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", utf8_content)