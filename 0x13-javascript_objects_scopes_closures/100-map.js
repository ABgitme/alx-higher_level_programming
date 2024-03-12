#!/usr/bin/node

const { list } = require('./100-data');
const computedArray = list.map((element, index) => element * index);
console.log(list);
console.log(computedArray);
