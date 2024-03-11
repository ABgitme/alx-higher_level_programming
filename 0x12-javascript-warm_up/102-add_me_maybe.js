#!/usr/bin/node
/**
 * Increments a number and calls a function with the incremented value.
 * @param {number} number - The number to increment.
 * @param {Function} theFunction - The function to call with the incremented value.
 */
function addMeMaybe (number, theFunction) {
  number += 1; // Increment the number
  theFunction(number); // Call the function with the incremented value
}

module.exports = { addMeMaybe }; // Exports the addMeMaybe function to make it visible from outside
