#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":
    # Set the letter as the parameter 'q'
    data = {"q": argv[1] if len(argv) > 1 else ""}
    
    # Send a POST request to the specified URL
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        # Try to parse the response JSON
        json_data = response.json()

        # Check if the JSON is properly formatted and not empty
        if isinstance(json_data, dict) and json_data:
            # Display the id and name in the specified format
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
        else:
            # Display No result if the JSON is empty
            print("No result")
    except ValueError:
        # Display Not a valid JSON if the JSON is invalid
        print("Not a valid JSON")
