#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};

// const Square = require('./5-square');

// const s1 = new Square(4);
// s1.print();
// s1.double();
// s1.print();
