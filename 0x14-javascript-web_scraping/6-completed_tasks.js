#!/usr/bin/node
const request = require('request');
const url = process.argv.slice(2)[0];
const dict = {};
request(url, function (error, response, body) {
  if (error) {
    throw error;
  }
  const content = JSON.parse(body);
  for (let i = 1; i <= 10; i++) {
    dict[i.toString()] = 0;
  }
  for (let i = 0; i < content.length; i++) {
    if (content[i].completed === true) {
      dict[content[i].userId.toString()]++;
    }
  }
  console.log(dict);
});
