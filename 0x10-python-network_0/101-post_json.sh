#!/bin/bash
# Sends a JSON POST request to the specified URL (provided as the first argument), includes a JSON file as data,
# and displays the body of the response.
curl -sX POST $1 -H "Content-Type: application/json" -d @$2 -L
