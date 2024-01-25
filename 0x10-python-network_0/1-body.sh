#!/bin/bash
# This script, when provided with a URL as an argument, utilizes the curl command to send a GET request to the specified URL.
# It then retrieves the response body size and displays it. The '-s' flag is used for silent mode, and '-X GET' specifies the HTTP request method.
# The '-L' flag follows any redirections that may occur during the request.
curl -sX GET $1 -L
