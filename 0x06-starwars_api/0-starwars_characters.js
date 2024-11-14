#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  characters.forEach((charUrl) => {
    request(charUrl, (err1, response1, body1) => {
      if (err1) {
        console.error(err1);
        return;
      }

      const character = JSON.parse(body1);
      console.log(character.name);
    });
  });
});

