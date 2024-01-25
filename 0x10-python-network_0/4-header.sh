#!/bin/bash
# Sends a GET request to the specified URL (provided as an argument), including a custom header, and displays the response body.
curl -sX GET $1 -H "X-HolbertonSchool-User-Id: 98" -L
