#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server supports
curl -sI -X OPTIONS "$1" | grep Allow: | awk '{$1=""; print $0}' | sed -e 's/ //'
