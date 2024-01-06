#!/bin/bash
# curl to send in a get request and print the body of respons
curl -s --json @"$2" "$1"
