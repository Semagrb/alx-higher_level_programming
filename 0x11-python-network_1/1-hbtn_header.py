#!/usr/bin/python3
"""
Python script that sends a request to a specified URL,
fetches the response, and displays the value of the
X-Request-Id variable found in the response header.
"""

from urllib import request
from sys import argv

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(argv) != 2:
        print("Usage: ./script.py <URL>")
    else:
        # Retrieve the URL from the command line
        url = argv[1]

        # Send a request to the specified URL
        with request.urlopen(url) as response:
            # Retrieve and display the value of the X-Request-Id variable from the header
            x_request_id = response.getheader("X-Request-Id")
            print(f"Value of X-Request-Id: {x_request_id}"
