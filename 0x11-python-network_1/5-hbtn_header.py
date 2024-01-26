#!/usr/bin/python3
"""
Python script that takes a URL as input, sends a GET request to the specified URL,
and displays the value of the X-Request-Id variable found in the response header.
"""

import requests
from sys import argv

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(argv) != 2:
        print("Usage: ./script.py <URL>")
    else:
        # Retrieve the URL from the command line
        url = argv[1]

        # Send a GET request to the specified URL using the requests library
        response = requests.get(url)

        # Retrieve and display the value of the X-Request-Id variable from the response header
        x_request_id = response.headers.get("X-Request-Id")
        print(f"Value of X-Request-Id: {x_request_id}")
