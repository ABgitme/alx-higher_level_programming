#!/bin/bash
# Send request to 0.0.0.0:5000/catch_me and capture the response
curl -s -X PUT -o /dev/null -w "You got me!" 0.0.0.0:5000/catch_me
