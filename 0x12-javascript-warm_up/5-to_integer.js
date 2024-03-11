#!/usr/bin/node

if (!isNaN(Number(process.argv[2]))) {
  const firstArg = process.argv[2];
  console.log('My number: ' + parseInt(firstArg));
} else {
  console.log('Not a number');
}
