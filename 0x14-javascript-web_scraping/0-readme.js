#!/usr/bin/node
const fs = require('fs');
const file = process.argv.slice(2)[0];
fs.readFile(file, 'utf-8', (error, text) => {
  if (error) {
    throw error;
  } else {
    console.log(text);
  }
});
