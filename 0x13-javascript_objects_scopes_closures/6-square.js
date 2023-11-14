#!/usr/bin/node
const Square0 = require('./5-square');
class Square extends Square0 {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (c === undefined) {
          process.stdout.write('X');
        } else {
          process.stdout.write(c);
        }
      }
      process.stdout.write('\n');
    }
  }
}
module.exports = Square;
