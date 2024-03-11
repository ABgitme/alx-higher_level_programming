#!/usr/bin/node

if (!isNaN(Number(process.argv[2]))) {
  const firstArg = process.argv[2];
  console.log('My number: ' + firstArg);
} else {
  console.log('No argument');
}
