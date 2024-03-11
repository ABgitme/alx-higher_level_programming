#!/usr/bin/node

if (!isNaN(Number(process.argv[2]))) {
  const firstArg = process.argv[2];
  for (let i = 0; i < parseInt(firstArg); i++) {
    let row = '';
    for (let j = 0; j < parseInt(firstArg); j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
