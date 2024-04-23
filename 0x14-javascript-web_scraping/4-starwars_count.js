#!/usr/bin/node
// test

const request = require('request');
const apiUrl = process.argv[2];
const characterID = '18';

function countMoviesWithWedge (apiUrl, characterID, callback) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      callback(new Error(error), null);
      return;
    }
    if (response.statusCode !== 200) {
      callback(new Error(`Failed to fetch movie data. Status code: ${response.statusCode}`), null);
      return;
    }
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach((film) => {
      const characters = film.characters;
      if (characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterID}/`)) {
        count++;
      }
    });
    callback(null, count);
  });
}

// Main execution
countMoviesWithWedge(apiUrl, characterID, (error, count) => {
  if (error) {
    console.error(error.message);
    return;
  }
  console.log(count);
});
