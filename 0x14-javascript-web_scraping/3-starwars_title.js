#!/usr/bin/node
const request = require('request');
const process = require('process');
const id = process.argv[2];
const movieURL = 'https://swapi-api.alx-tools.com/api/films/' + id;
request(movieURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
