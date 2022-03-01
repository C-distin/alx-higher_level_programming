#!/usr/bin/node
const myVar = process.argv[2];
const convertNumber = Math.floor(Number(myVar));
if (isNaN(convertNumber)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < convertNumber; i++) {
    let output = '';
    for (let j = 0; j < convertNumber; j++) {
      output += 'X';
    }
    console.log(output);
  }
}
