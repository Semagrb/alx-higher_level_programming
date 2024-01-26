#!/usr/bin/python3
"""
Sends a request to a specified URL, fetches the response body,
and displays the content.

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors gracefully.
"""

import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
    else:
        # Retrieve the URL from the command line
        url = sys.argv[1]

        # Create a request for the specified URL
        request = urllib.request.Request(url)

        try:
            # Attempt to open the URL and fetch the response
            with urllib.request.urlopen(request) as response:
                # Display the content of the response
                print(response.read().decode("ascii"))
        except urllib.error.HTTPError as e:
            # Handle HTTP errors gracefully and display the error code
            print("Error code: {}".format(e.code))
