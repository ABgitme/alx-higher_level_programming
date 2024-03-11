#!/usr/bin/node

// Iterate through each command-line argument
// Access arguments using process.argv (without 'var')
const firstArg = process.argv[2];
const secondArg = process.argv[3];

// Print arguments with a space (" ") before "is"
console.log(`${firstArg} is ${secondArg}`);
