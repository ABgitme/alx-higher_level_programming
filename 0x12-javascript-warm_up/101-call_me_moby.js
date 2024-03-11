#!/usr/bin/node

/**
 * Executes a function x times.
 * @param {number} x - The number of times to execute the function.
 * @param {Function} theFunction - The function to execute.
 */
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports = { callMeMoby }; // Exports the callMeMoby function to make it visible from outside
