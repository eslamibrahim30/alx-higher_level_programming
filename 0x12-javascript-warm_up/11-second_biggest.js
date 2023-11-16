#!/usr/bin/node
let value1 = parseInt(process.argv[2]);
let value2 = parseInt(process.argv[2]);
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) >= value1) {
      value1 = parseInt(process.argv[i]);
    } 
  }
  if (value1 === value2) {
    value2 = parseInt(process.argv[3]);
  }
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) >= value2 && parseInt(process.argv[i]) < value1) {
      value2 = parseInt(process.argv[i]);
    }
  }
  console.log(value2);
}
