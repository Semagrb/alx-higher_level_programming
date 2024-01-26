#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
    else:
        # Retrieve the URL from the command line
        url = sys.argv[1]

        # Create a GET request for the specified URL
        request = urllib.request.Request(url)

        try:
            # Open the URL and retrieve the response
            with urllib.request.urlopen(request) as response:
                # Extract the X-Request-Id header variable and display its value
                x_request_id = dict(response.headers).get("X-Request-Id")
                print(x_request_id)
        except urllib.error.HTTPError as e:
            # Handle HTTP errors gracefully and display the error code
            print(f"Error code: {e.code}")
