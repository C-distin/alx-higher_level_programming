#!/usr/bin/node
const myVar = process.argv;
if (myVar.length > 2) {
  console.log('Argument found');
} else {
  console.log('No argument found');
}
