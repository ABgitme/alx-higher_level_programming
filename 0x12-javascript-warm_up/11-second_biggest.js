#!/usr/bin/node

/**
 * Searches for the second biggest integer in the list of arguments.
 * @param {number[]} args - The list of arguments to search through.
 * @returns {number} - The second biggest integer.
 */
const secondBiggest = (args) => {
  if (args.length <= 1) {
    return 0;
  }

  let firstMax = -Infinity;
  let secondMax = -Infinity;

  for (let i = 0; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (num > firstMax) {
      secondMax = firstMax;
      firstMax = num;
    } else if (num > secondMax && num < firstMax) {
      secondMax = num;
    }
  }

  return secondMax;
};

const args = process.argv.slice(2); // Retrieves the list of arguments, excluding the first two (script name and interpreter)
const result = secondBiggest(args); // Finds the second biggest integer
console.log(result); // Prints the result
