#!/bin/bash
# Send an OPTIONS request to the URL to get allowed methods
curl -s -i -X OPTIONS "$1" | grep -iE '^Allow:' | sed 's/Allow: //i'
