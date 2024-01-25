#!/bin/bash
# Sends a request to the specified URL (provided as an argument) and outputs only the status code of the response.
curl -o /dev/null -sw "%{http_code}" $1
