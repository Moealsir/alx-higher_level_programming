#!/usr/bin/node
// test

const fs = require('fs');
const { argv } = require('process');

const filename = argv[2];
const content = argv[3];

fs.writeFile(filename, content, err => {
  if (err) {
    console.log(err);
    return;
  }
});
