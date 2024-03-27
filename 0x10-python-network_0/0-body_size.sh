#!/usr/bin/env bash
# This script will print the size of the body of the response

set -x

curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
