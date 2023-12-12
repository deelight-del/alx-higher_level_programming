#!/usr/bin/node
exports.logMe = function (item) {
  if (!exports.logMe.staticVariable && exports.logMe.staticVariable !== 0) {
    exports.logMe.staticVariable = 0;
    process.stdout.write(String(exports.logMe.staticVariable));
    process.stdout.write(': ');
    console.log(item);
  } else {
    exports.logMe.staticVariable++;
    process.stdout.write(String(exports.logMe.staticVariable));
    process.stdout.write(': ');
    console.log(item);
  }
};
