#!/usr/bin/node

/**
 * Computes the factorial of an integer recursively.
 * @param {number} n - The integer for which to compute the factorial.
 * @returns {number} - The factorial of n.
 */
const factorial = (n) => {
  if (isNaN(n)) {
    return 1;
  }

  n = parseInt(n);

  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
};

const input = process.argv[2];
const result = factorial(input);
console.log(result);
