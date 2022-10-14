#!/usr/bin/node
exports.converter = function (base) {
  return num => num.toString(base);
};

// const converter = require('./10-converter').converter;

// let myConverter = converter(10);

// console.log(myConverter(2));
// console.log(myConverter(12));
// console.log(myConverter(89));

// myConverter = converter(16);

// console.log(myConverter(2));
// console.log(myConverter(12));
// console.log(myConverter(89));
