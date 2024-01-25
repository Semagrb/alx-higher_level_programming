#!/bin/bash
# Sends a POST request to the specified URL (provided as an argument) with predefined data, and displays the response body.
curl -sX POST $1 -d "email=test@gmail.com&subject=I will always be here for PLD" -L
