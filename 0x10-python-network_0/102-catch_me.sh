#!/bin/bash
# Send request to 0.0.0.0:5000/catch_me and capture the response
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
