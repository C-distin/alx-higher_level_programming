#!/usr/bin/node
const myVar = process.argv;
if (myVar[2] != null) {
  console.log(myVar[2]);
} else {
  console.log('No argument found');
}
