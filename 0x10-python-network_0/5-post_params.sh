#!/bin/bash
# curl to send in a get request and print the body of respons
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1";
