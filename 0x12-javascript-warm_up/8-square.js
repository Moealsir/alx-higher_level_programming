#!/usr/bin/node
// square
const size = parseInt(process.argv[2]);

if (isNaN(size) || size < 0) {
  console.log();
} else {
  for (let i = 0; i < size; i++) { console.log('X'.repeat(size)); }
}
