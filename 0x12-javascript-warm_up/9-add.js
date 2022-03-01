#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const myVar1 = process.argv[2];
const myVar2 = process.argv[3];
console.log(add(Number(myVar1), Number(myVar2)));
