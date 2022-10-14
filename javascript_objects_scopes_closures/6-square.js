#!/usr/bin/node
const square = require('./5-square');

module.exports = class Square extends square {
  charPrint (C) {
    if (C === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(C.repeat(this.width));
      }
    }
  }
};

// const s1 = new Square(4);
// s1.charPrint();

// s1.charPrint('C');
