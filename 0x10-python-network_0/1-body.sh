#!/bin/bash
# Fetches the body size of a URL's response using curl in silent mode, following any redirections.
curl -sX GET $1 -L
