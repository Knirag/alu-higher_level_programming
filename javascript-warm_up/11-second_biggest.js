#!/usr/bin/node
const argsArray = process.argv.slice(2);
if (argsArray.length <= 1) {
  console.log('0');
} else {
  argsArray.sort((a, b) => (a - b));
  argsArray.pop();
  console.log(argsArray.pop());
}
