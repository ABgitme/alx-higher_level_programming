#!/bin/bash
# Extract Content-Length from the response headers
curl -sI "$1" | grep -iE '^Content-Length:' | awk '{print $2}'
