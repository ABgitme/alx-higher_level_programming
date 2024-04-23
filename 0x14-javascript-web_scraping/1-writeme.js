#!/usr/bin/node
const fs = require('fs');

// Get the file path and string from the command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Check if both file path and content are provided as arguments
if (!filePath || !content) {
  process.exit(1);
}

// Write the content to the file
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
