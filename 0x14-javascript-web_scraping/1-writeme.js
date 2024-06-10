#!/usr/bin/node
const fs = require('fs');
const file = process.argv.slice(2)[0];
const content = process.argv.slice(2)[1];
fs.writeFile(file, content, (error) => {
  if (error) {
    throw error;
  }
});
