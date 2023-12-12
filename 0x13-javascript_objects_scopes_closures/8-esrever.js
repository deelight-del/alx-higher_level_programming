#!/usr/bin/node
exports.esrever = function (list) {
  const Length = list.length;
  const newArray = [];
  for (let i = 0; i < Length; i++) {
    newArray[i] = list[Length - 1 - i];
  }
  return newArray;
};
