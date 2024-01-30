#!/usr/bin/node
const request = require('request');
const process = require('process');
const urlPath = process.argv[2];
request(urlPath, function (error, response, body) {
  try {
    console.log('code:', response.statusCode);
  }
});
