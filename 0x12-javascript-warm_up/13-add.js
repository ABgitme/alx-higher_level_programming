#!/usr/bin/node

/**
 * Adds two integers and returns the result.
 * @param {number} a - The first integer.
 * @param {number} b - The second integer.
 * @returns {number} - The sum of a and b.
 */
function add (a, b) {
  return a + b;
}

module.exports = { add }; // Exports the add function to make it visible from outside
