#!/usr/bin/node
// Check the number of arguments passed to the script
const argsCount = process.argv.length - 2; // Subtracting 2 to exclude 'node' and the script filename

// Print messages based on the number of arguments
if (argsCount === 0) {
  console.log('No argument');
} else if (argsCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
