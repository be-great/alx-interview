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
  const characterUrls = movie.characters;

  // Create an array of Promises for each character request
  const characterPromises = characterUrls.map((charUrl) => {
    return new Promise((resolve, reject) => {
      request(charUrl, (err, response, body) => {
        if (err) {
          reject(err);
        } else {
          const character = JSON.parse(body);
          resolve(character.name);
        }
      });
    });
  });

  // Wait for all character requests to complete
  Promise.all(characterPromises)
    .then((characterNames) => {
      characterNames.forEach((name) => {
        console.log(name);
      });
    })
    .catch((error) => {
      console.error('Error fetching character names:', error);
    });
});
