#!/usr/bin/node
const firstArg = process.argv[2];
const secondArg = process.argv[3];
function add (a, b) {
  const c = Number(a) + Number(b);
  return c;
}
console.log(`${add(firstArg, secondArg)}`);
