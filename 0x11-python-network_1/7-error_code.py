#!/usr/bin/python3
"""
Sends a GET request to a specified URL and displays the response body.

Usage: ./7-error_code.py <URL>
  - Handles HTTP errors gracefully.
"""

import sys
import requests

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: ./7-error_code.py <URL>")
    else:
        # Retrieve the URL from the command line
        url = sys.argv[1]

        # Send a GET request to the specified URL using the requests library
        response = requests.get(url)

        # Check if the response status code indicates an error
        if response.status_code >= 400:
            # Handle HTTP errors and display the error code
            print("Error code: {}".format(response.status_code))
        else:
            # Display the content of the response body
            print(response.text)
