#!/usr/bin/node
const { dict } = require('./101-data');

// Create an empty object to store the new dictionary
const occurrencesById = {};

// Iterate over the keys and values of the original dictionary
for (const userId in dict) {
  const occurrences = dict[userId];

  // Check if the occurrences is already a key in the new dictionary
  if (!occurrencesById[occurrences]) {
    // If not, initialize it as an empty array
    occurrencesById[occurrences] = [];
  }

  // Push the userId to the list of user ids for the corresponding occurrences
  occurrencesById[occurrences].push(userId);
}

// Print the new dictionary
console.log(occurrencesById);
