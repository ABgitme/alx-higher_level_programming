#!/usr/bin/node

if (!isNaN(Number(process.argv[2]))) {
  const firstArg = process.argv[2];
  for (let i = 0; i < parseInt(firstArg); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
