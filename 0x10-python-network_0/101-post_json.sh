#!/bin/bash
# Send POST request to the URL with the contents of the file in the body of the request
curl -s -X POST -d @"$2" -H "Content-Type: application/json" "$1"
