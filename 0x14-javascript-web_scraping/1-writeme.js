#!/usr/bin/node
const fs = require('fs');

// Get the file path and string from the command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the content to the file
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
