#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  let count = number;
  count++;
  theFunction(count);
};
