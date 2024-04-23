#!/usr/bin/node
// test

const fs = require('fs');
const { argv } = require('process');

const filename = argv[2];
const content = argv[3];

fs.writeFile(filename, content, 'utf-8', (err) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(content);
});
