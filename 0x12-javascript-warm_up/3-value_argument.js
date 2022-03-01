#!/usr/bin/node
const myVar = process.argv;
console.log(typeof myVar[2] === 'undefined' ? 'No argument' : myVar[2]);
