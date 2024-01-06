#!/bin/bash
# curl to send in a get request and print the body of respons
response=$(curl -G -s -w "%{http_code}" -o /dev/null "$1")
if [ "$response" = "200" ]; then
	curl -G -s "$1";
fi
