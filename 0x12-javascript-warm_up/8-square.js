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
    const repeatedStr = 'X'.repeat(loopTimes);
    console.log(repeatedStr);
  }
} else {
  console.log('Missing size');
}
