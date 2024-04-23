#!/usr/bin/node
// test

const { writeFile } = require('fs');
const { get } = require('request');
const apiUrl = process.argv[2];
const filepath = process.argv[3];

get(apiUrl, (err, body) => {
  if (err) {
    console.log(err);
    return;
  }
  writeFile(filepath, body, 'utf8', err => {
    if (err) {
      console.log(err);
    }
  });
});
