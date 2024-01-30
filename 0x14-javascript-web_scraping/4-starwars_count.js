#!/usr/bin/node
const request = require('request');
const process = require('process');
const id = 18;
const idURL = 'https://swapi-api.alx-tools.com/api/people/' + id + '/';
const filmURL = process.argv[2];
let count = 0;
request(filmURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = (JSON.parse(body)).results;
    for (let i = 0; i < films.length; i++) {
      if (films[i].characters.includes(idURL)) {
        count++;
      }
    }
    console.log(count);
  }
});
