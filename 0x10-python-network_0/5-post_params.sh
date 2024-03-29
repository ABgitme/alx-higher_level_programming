#!/bin/bash
# Set the variables for email and subject
email="test@gmail.com"
subject="I will always be here for PLD"
# Send POST request to the URL with variables and display the body of the response
curl -s -X POST -d "email=$email&subject=$subject" "$1"
