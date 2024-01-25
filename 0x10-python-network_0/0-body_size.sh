#!/bin/bash

# Take in a URL as a command line argument
url=$1

# If no URL is provided, print a usage message and exit the script
if [ -z "$url" ]; then
 echo "Usage: $0 <URL>"
 exit 1
fi

# Send a GET request to the specified URL with the '-s' flag to make the request silent
# and the '-I' flag to make a HEAD request instead of a GET request.
# This means we're only retrieving the headers of the response, not the body.
curl_response=$(curl -sI "$url")

# Check if the 'Content-Length' header is present in the response.
# If it is, the 'grep' command will return a non-empty string.
if echo "$curl_response" | grep -q "Content-Length"; then
 # If the 'Content-Length' header is present, extract its value using 'cut'.
 # The '-d " "' flag tells 'cut' to use spaces as the delimiter,
 # the '-f2' flag tells 'cut' to extract the second field,
 # which is the value of the 'Content-Length' header.
 content_length=$(echo "$curl_response" | grep "Content-Length" | cut -d " " -f2)

 # If the 'Content-Length' header is not present, print an error message.
else
 echo "Error: The 'Content-Length' header is not present in the response."
 exit 1
fi

# Finally, print the size of the body of the response, which is the value of the 'Content-Length' header.
echo "The size of the body of the response is $content_length bytes."
