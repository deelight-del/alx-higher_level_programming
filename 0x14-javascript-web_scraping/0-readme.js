#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const filePath = process.argv[2];
fs.readFile(filePath, function (err, data) {
  try {
    console.log(data.toString());
  } catch (error) {
    console.log(err);
  }
});
