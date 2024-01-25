#!/bin/bash

# Check if URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from command line arguments
url=$1

# Use curl to send a request and display the size of the response body in bytes
size=$(curl -sI $url | grep -i "content-length" | awk '{print $2}' | tr -d '\r\n')

echo $size
