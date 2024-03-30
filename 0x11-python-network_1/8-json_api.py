#!/usr/bin/python3
"""
Module: search_user

Description:
This script takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter.
If the letter is not provided, it sets the parameter q="".
If the response body is properly JSON formatted and not empty,
    it displays the id and name.
Otherwise, it displays appropriate error messages.

Usage:
./search_user.py <letter>

Arguments:
- <letter>: The letter to be sent as a parameter in the POST request.
    If not provided, defaults to an empty string.

Requirements:
- Uses the packages requests and sys.
- Does not import packages other than requests and sys.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': q})
    json_response = response.json()
    try:
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except Exception.invalid_response:
        print("Not a valid JSON")
