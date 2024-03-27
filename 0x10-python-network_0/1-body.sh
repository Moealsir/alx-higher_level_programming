#!/bin/bash
# This script sends a GET request to the URL and displays the body of the response if the status code is 200
curl -s -X GET -i "$1" | awk 'BEGIN {body=0} {if (body) print} /HTTP\/1.1 200 OK/{body=1}'
