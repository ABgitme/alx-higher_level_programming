#!/usr/bin/python3
"""
Module: 4-hbtn_status

Description:
This script fetches the status of
    https://alx-intranet.hbtn.io/status using the requests package.
It displays information about the response body in the
    specified format.

Usage:
./4-hbtn_status.py | cat -e

Output Format:
- Body response:
    - type: <class 'str'>
    - content: OK
"""
import requests


url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)

print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
