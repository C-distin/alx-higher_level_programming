#!/bin/bash
# Script to take in a URL, send a GET request to the URL, and display the size of the body of the response
curl -sfL "$1" -X GET
