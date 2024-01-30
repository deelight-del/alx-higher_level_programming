#!/usr/bin/node
const request = require('request');
const process = require('process');
const urlPath = process.argv[2];
request
  .get(urlPath)
  .on('response', function (response) {
    console.log('code:', response.statusCode);
  });
