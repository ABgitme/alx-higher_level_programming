#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command line arguments
const movieID = process.argv[2];

// Star Wars API URL to get movie details
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Make a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const movie = JSON.parse(body);

  // Print each character's name
  movie.characters.forEach(characterUrl => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }
      if (response.statusCode !== 200) {
        console.error(`Error: Status code ${response.statusCode}`);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
