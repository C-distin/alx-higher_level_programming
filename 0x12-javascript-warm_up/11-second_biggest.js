#!/usr/bin/node

const arrayNums = process.argv.slice(2);
function SecondBiggest (newArray) {
  if (newArray.length < 2) {
    return (0);
  } else {
    let biggest = newArray[0];
    let secondBiggest = newArray[0];
    for (let i = 0; i < newArray.length; i++) {
      if (newArray[i] > biggest) {
        secondBiggest = biggest;
        biggest = newArray[i];
      } else if (newArray[i] > secondBiggest && newArray[i] !== biggest) {
        secondBiggest = newArray[i];
      }
    }
    return (secondBiggest);
  }
}
console.log(SecondBiggest(arrayNums));
