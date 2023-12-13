#!/usr/bin/node
const fs = require('fs');
function concatFiles (file1, file2, outFile) {
  fs.readFile(file1, 'utf8', (err, data1) => {
    if (err) {
      console.log('error');
      return;
    }
    fs.readFile(file2, 'utf8', (err, data2) => {
      if (err) {
        console.log('error');
        return;
      }
      const outData = data1 + data2;
      fs.writeFile(outFile, outData, 'utf8', (err, data3) => {
        if (err) {
          console.log('error');
        }
      });
    });
  });
}

const argv = process.argv;
concatFiles(argv[2], argv[3], argv[4]);
