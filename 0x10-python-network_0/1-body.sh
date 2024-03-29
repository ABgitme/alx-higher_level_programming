#!/bin/bash
# Send request to the URL and save the response body to a variable
curl -sX GET "$1" -L
