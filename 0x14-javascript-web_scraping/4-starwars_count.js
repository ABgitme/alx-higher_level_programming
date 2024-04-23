#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the provided Star Wars API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movies = JSON.parse(body).results;
  const count = movies.reduce((acc, movie) => {
    if (movie.characters.some(character => character.endsWith('/18/'))) {
      return acc + 1;
    }
    return acc;
  }, 0);

  console.log(count);
});
