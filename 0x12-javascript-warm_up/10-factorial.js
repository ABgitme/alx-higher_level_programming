#!/usr/bin/node

/**
 * Computes the factorial of an integer recursively.
 * @param {number} n - The integer for which to compute the factorial.
 * @returns {number} - The factorial of n.
 */
function factorial (n) {
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
}

const input = Number(process.argv[2]); // Retrieves the number from command line argument
console.log(factorial(input)); // Prints the factorial of the input number
