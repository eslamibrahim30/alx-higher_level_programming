#!/usr/bin/node
const Square0 = require('./5-square');
class Square extends Square0 {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        if (c == null) {
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
