#!/bin/bash
# curl to send in a get request and print the body of respons
curl -sI -w "%{http_code}" "$1" -o /dev/null
