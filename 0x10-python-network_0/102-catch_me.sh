#!/bin/bash
# Send request to 0.0.0.0:5000/catch_me and capture the response
curl -s -X PUT -w "You find me!" -o /dev/null -N 0.0.0.0:5000/catch_me
