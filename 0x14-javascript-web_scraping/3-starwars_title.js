#!/usr/bin/node
const request = require('request');
const root = 'https://swapi-api.alx-tools.com/api/films/';
const url = root + process.argv.slice(2)[0];
request(url, function (error, response, body) {
  if (error) {
    throw error;
  }
  console.log(JSON.parse(body).title);
});
