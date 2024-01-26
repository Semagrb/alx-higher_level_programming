#!/usr/bin/python3
"""
Sends a POST request to a specified URL with a provided email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    # Check if both URL and email are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
    else:
        # Retrieve the URL and email from command-line arguments
        url = sys.argv[1]
        email = sys.argv[2]

        # Prepare the data to be sent in the POST request
        values = {"email": email}
        data = urllib.parse.urlencode(values).encode("ascii")

        # Create a POST request and send it to the specified URL
        request = urllib.request.Request(url, data)
        with urllib.request.urlopen(request) as response:
            # Display the body of the response
            print(response.read().decode("utf-8"))
