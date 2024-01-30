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
    const characters = data.characters;
    for (let i = 0; i < characters.length; i++) {
      const characterApi = characters[i];
      request(characterApi, function (err, resp, bod) {
        if (err) {
          console.log(err);
        } else {
          const character = JSON.parse(bod);
          console.log(character.name);
        }
      });
    }
  }
});
