#!/usr/bin/node
const request = require('request');
const url = process.argv.slice(2)[0];
const search = 'https://swapi-api.alx-tools.com/api/people/18/';
let counter = 0;
request(url, function (error, response, body) {
  if (error) {
    throw error;
  }
  const content = JSON.parse(body).results;
  for (let i = 0; i < content.length; i++) {
    if (content[i].characters.includes(search)) {
      counter++;
    }
  }
  console.log(counter);
});
