#!/bin/bash
# curl to send in a get request and print the body of respons
curl -s -I "$1" | grep -i '^Allow:' | cut -d' ' -f2-;
