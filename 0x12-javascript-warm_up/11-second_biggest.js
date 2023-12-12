#!/usr/bin/node
let argArray = process.argv;
let Biggest;
let secondBiggest;
if (argArray.length < 4) {
  console.log(0);
} else {
  argArray = argArray.slice(2);

  if (Number(argArray[0]) > Number(argArray[1])) {
    Biggest = Number(argArray[0]);
    secondBiggest = Number(argArray[1]);
  } else {
    Biggest = Number(argArray[1]);
    secondBiggest = Number(argArray[0]);
  }
  for (const value of argArray) {
    if (Number(value) >= secondBiggest && Number(value) < Biggest) {
      secondBiggest = Number(value);
    } else if (Number(value) > Biggest) {
      secondBiggest = Biggest;
      Biggest = Number(value);
    }
  }
  console.log(secondBiggest);
}
