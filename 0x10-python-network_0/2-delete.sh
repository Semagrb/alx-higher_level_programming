#!/bin/bash
# Initiates a DELETE request to the specified URL (provided as the first argument) using curl and displays the response body.
curl -sX DELETE $1 -L
