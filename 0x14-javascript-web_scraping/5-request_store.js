#!/usr/bin/node
const request = require('request');
const process = require('process');
const fs = require('fs');
const url = process.argv[2];
const outFilePath = process.argv[3];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = body.toString();
    fs.writeFile(outFilePath, data, 'utf8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
