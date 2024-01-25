#!/bin/bash

# Check if a URL was provided as an argument
if [ -z "$1" ]
then
  echo "No URL provided. Please run the script with a URL as an argument."
  exit 1
fi

# Send a GET request to the URL and store the response in a variable
response=$(curl -s $1)

# Display the size of the body of the response in bytes
echo "Size of the body of the response (in bytes): $(echo ${#response}))"
