#!/usr/bin/node
const argvTwo = process.argv[2];

function isNumber (number) {
  if (isNaN(number)) {
    return false;
  } else {
    return true;
  }
}

if (isNumber(argvTwo)) {
  const loopTimes = Number(argvTwo);
  for (let i = 0; i < loopTimes; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
