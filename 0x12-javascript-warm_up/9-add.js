#!/usr/bin/node
// add
const firstInt = parseInt(process.argv[2]);
const secInt = parseInt(process.argv[3]);

if (isNaN(firstInt) || isNaN(secInt)) {
  console.log('NaN');
} else {
  const sum = firstInt + secInt;
  console.log(sum);
}
