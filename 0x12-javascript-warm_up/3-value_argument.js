#!/usr/bin/node

// Check if no arguments are passed
let counter = 0;

// Iterate through each command-line argument
process.argv.forEach((arg, index) => {
  if (index === 2) {
    console.log(arg);
  }
  counter = counter + 1;
});

// If no arguments are passed, print "No argument"
if (counter <= 2) {
  console.log('No argument');
}
