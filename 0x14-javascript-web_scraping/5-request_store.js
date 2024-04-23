#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Check if both URL and file path are provided as arguments
if (!url || !filePath) {
  console.error('Please provide both the URL and the file path as arguments.');
  process.exit(1);
}

// Make a GET request to the provided URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    // Write the response body to the specified file path
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
