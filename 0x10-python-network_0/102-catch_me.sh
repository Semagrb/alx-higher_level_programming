#!/bin/bash
# Triggers a request to 0.0.0.0:5000/catch_me, prompting the server to respond with the message "You got me!" in the response body.
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
