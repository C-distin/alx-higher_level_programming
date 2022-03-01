#!/usr/bin/node
const myVar = process.argv[2];
const convertNumber = Math.floor(Number(myVar));
if (isNaN(convertNumber)) {
  console.log('Not a number');
} else {
  for (let i = 0; i < convertNumber; i++) {
    console.log('C is fun');
  }
}
