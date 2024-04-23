#!/usr/bin/node
// test

const request = require('request');
const movieID = process.argv[2];
const apiurl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(apiurl, (error, Response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  if (Response.statusCode !== 200) {
    console.log(`Failed to fetch movie details. Status code: ${Response.statusCode}`);
    return;
  }

  const movieData = JSON.parse(body);
  console.log(movieData.title);
});
