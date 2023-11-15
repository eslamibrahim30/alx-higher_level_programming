#!/usr/bin/node
if (Number.isInteger(parseInt(process.argv[2])) && Number.isInteger(parseInt(process.argv[3]))) {
  console.log(parseInt(process.argv[2]) + parseInt(process.argv[3]));
} else {
  console.log('NaN');
}
