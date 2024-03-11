#!/usr/bin/node

// Check if no arguments are passed
if (process.argv.length <= 2) {
  console.log('No argument');
}
  // Iterate through each command-line argument
  process.argv.forEach((arg, index) => {
    if (index === 2) {
      console.log(arg);
    }
  });
