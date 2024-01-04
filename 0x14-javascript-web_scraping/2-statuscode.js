#!/usr/bin/node
const request = require('request');
const url = process.argv.slice(2)[0];
request(url, function (error, response, body) {
  if (error) {
    throw error;
  }
  console.log('code: ' + response.statusCode);
});
