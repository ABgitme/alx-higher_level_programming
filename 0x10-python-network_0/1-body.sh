#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to the URL and save the response body to a variable
response=$(curl -sX GET "$1" -L)
echo "$response"
