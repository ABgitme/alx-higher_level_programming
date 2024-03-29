#!/bin/bash
# Send request to 0.0.0.0:5000/catch_me and capture the response
curl -s -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"