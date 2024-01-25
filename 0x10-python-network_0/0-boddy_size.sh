#!/bin/bash

# Check if the 'url' variable is empty.
# If it is, print a usage message and exit the script.
if [ -z "$url" ]; then
 echo "Usage: $0 <URL>"
 exit 1
fi

# Send a GET request to the specified URL using the 'curl' command.
# The '-D-' flag tells 'curl' to send the headers of the response to stdout,
# the '-s' flag tells 'curl' to work silently,
# and the '-I' flag tells 'curl' to make a HEAD request instead of a GET request.
# This means we're only retrieving the headers of the response, not the body.
curl_response=$(curl -D- -s -I "$url")

# Extract the value of the 'Content-Length' header from the response using 'grep' and 'cut'.
content_length=$(echo "$curl_response" | grep "Content-Length" | cut -d " " -f2)

# If the 'Content-Length' header is not present, print an error message.
if [ -z "$content_length" ]; then
 echo "Error: The 'Content-Length' header is not present in the response."
 exit 1
fi

# Finally, print the size of the body of the response, which is the value of the 'Content-Length' header.
echo "The size of the body of the response is $content_length bytes."
