#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Check if an API URL is provided as an argument
if (!apiUrl) {
  console.error('Please provide the API URL as an argument.');
  process.exit(1);
}

// Character ID for Wedge Antilles
const characterId = '18';

// Make a GET request to the provided Star Wars API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    // Count the number of movies where Wedge Antilles is present
    const moviesWithWedge = films.filter(film =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    ).length;
    console.log(`${moviesWithWedge}`);
  }
});
