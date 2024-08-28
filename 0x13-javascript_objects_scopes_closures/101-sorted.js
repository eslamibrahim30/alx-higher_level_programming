#!/usr/bin/node
const { dict } = require('./101-data.js');
const newDict = {};
for (const [key, value] of Object.entries(dict)) {
  if (!(Object.prototype.hasOwnProperty.call(newDict, value))) {
    newDict[value] = [];
  }
  newDict[value].push(key);
}
console.log(newDict);
