#!/usr/node

const number = parseInt(process.argv[2], 10);
function factorial (number) {
  if (isNaN(number) || number === 0) {
    return (1);
  }
  const result = number * factorial(number - 1);
  return (result);
}
console.log(factorial(number));
