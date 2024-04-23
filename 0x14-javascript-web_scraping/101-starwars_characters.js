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

  // Define a function to recursively print characters
  const printCharacters = (index) => {
    if (index >= movie.characters.length) {
      return;
    }
    const characterUrl = movie.characters[index];
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
      printCharacters(index + 1); // Recursively call for the next character
    });
  };

  // Start printing characters
  printCharacters(0);
});
