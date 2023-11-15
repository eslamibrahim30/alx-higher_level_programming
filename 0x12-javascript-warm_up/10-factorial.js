#!/usr/bin/node
function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
if (Number.isInteger(parseInt(process.argv[2]))) {
  console.log(factorial(parseInt(process.argv[2])));
} else if (process.argv.length === 2) {
  console.log(1);
}
