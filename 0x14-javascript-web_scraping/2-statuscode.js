#!/usr/bin/node
// terst

const request = require('request');
const url = process.argv[2];

request(url, (error, Response) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code:', Response.statusCode);
});
