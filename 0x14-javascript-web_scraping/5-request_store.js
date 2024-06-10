#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv.slice(2)[0];
const file = process.argv.slice(2)[1];
request(url, function (error, response, body) {
  if (error) {
    throw error;
  }
  fs.writeFile(file, body, (error) => {
    if (error) {
      throw error;
    }
  });
});
