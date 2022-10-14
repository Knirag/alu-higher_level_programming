#!/usr/bin/node
let value = 0;
exports.logMe = function (item) {
  console.log(value + ': ' + item);
  value += 1;
};

// const logMe = require('./9-logme').logMe;

// logMe("Hello");
// logMe("Best");
// logMe("School");
