#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to the URL and save the response body to a temporary file
response=$(curl -s -o /tmp/response_body "$1")

# Check if curl command was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to fetch URL"
    exit 1
fi

# Get the size of the response body file in bytes
size=$(stat -c %s /tmp/response_body)

echo "$size"

# Clean up temporary file
rm /tmp/response_body
