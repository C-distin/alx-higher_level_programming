#!/bin/bash
# Script to take in a URL, send a request to that URL, and display the size of the body of the response
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2