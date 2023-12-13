#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const key of Object.keys(dict)) {
  const value = dict[key];
  if (value in newDict) {
    newDict[value].push(key);
  } else {
    newDict[value] = [key];
  }
}

console.log(newDict);
