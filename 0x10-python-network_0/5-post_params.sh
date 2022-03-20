#!/bin/bash
# Script that accepts a URL as an argument, sends a POST request to the URL, and displays the body of the response
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
