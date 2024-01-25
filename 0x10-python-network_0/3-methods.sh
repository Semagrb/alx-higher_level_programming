#!/bin/bash
# Retrieves and displays the HTTP methods accepted by the server for the specified URL.
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
