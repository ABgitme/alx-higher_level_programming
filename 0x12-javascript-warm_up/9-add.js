#!/usr/bin/node

if (!isNaN(Number(process.argv[2])) && !isNaN(Number(process.argv[3]))) {
  const firstArg = process.argv[2];
  const secondArg = process.argv[3];
  const sum = parseInt(firstArg) + parseInt(secondArg);
  console.log(sum);
} else {
  console.log('NaN');
}
