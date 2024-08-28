#!/usr/bin/node
const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
fs.readFile(fileA, 'utf8', (err, inputA) => {
  if (err) throw err;
  const fileAtext = inputA.toString();
  fs.readFile(fileB, 'utf8', (err, inputB) => {
    if (err) throw err;
    const fileBtext = inputB.toString();
    const fileCtext = fileAtext + fileBtext;
    fs.writeFile(fileC, fileCtext, (err) => {
      if (err) throw err;
    });
  });
});
