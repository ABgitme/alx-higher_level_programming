#!/bin/bash
response=$(curl -sI "$1")

# Extract Content-Length from the response headers
content_length=$(echo "$response" | grep -iE '^Content-Length:' | awk '{print $2}')
echo "$content_length"
