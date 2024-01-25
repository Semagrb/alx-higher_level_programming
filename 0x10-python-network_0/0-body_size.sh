#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the URL and display the size of the response body in bytes
curl -sI "$1" | grep -i "Content-Length" | cut -d " " -f2
