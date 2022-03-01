#!/usr/bin/node
const myVar = process.argv[2];
const convertNumber = Math.floor(Number(myVar));
console.log(isNaN(convertNumber) ? 'Not a number' : 'My number: ' + convertNumber);
