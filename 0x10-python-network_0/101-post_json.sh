#!/bin/bash
# curl to send in a get request and print the body of respons
curl -s -H "content-Type: apllication/json" --data-binary @"$2" -X POST "$1";
