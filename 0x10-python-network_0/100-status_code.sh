#!/bin/bash
# Send request to the URL and save the status code to a variable
curl -s -o /dev/null -w "%{http_code}" "$1"
