#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command line arguments
const movieID = process.argv[2];

// Construct the URL with the provided movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Make a GET request to the Star Wars API
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const film = JSON.parse(body);
      console.log(`Title: ${film.title}`);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
