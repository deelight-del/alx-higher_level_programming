#!/usr/bin/node
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    let printString;
    if (c) {
      printString = String(c).repeat(this.width);
    } else {
      printString = 'X'.repeat(this.width);
    }
    for (let i = 0; i < this.height; i++) {
      console.log(printString);
    }
  }
}

module.exports = Square;
