#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Initialize a counter for occurrences
  let occurrences = 0;

  // Iterate through the list
  for (let i = 0; i < list.length; i++) {
    // Check if the current element is equal to the searchElement
    if (list[i] === searchElement) {
      // Increment the counter if there's a match
      occurrences++;
    }
  }

  // Return the total number of occurrences
  return occurrences;
};
