#!/usr/bin/node
if (Number.isInteger(parseInt(process.argv[2]))) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
} else {
  console.log('Missing size');
}
