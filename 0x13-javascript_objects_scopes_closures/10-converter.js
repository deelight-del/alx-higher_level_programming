#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    console.log(number.toString(base));
  };
};
