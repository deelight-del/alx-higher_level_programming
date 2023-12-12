#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let Count = 0;
  for (const value of list) {
    if (value === searchElement) {
      Count++;
    }
  }
  return Count;
};
