#!/usr/bin/node

// This script search for a particular movie title from the star wars api
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  // converting the response to a Javascript object
  const data = JSON.parse(body);
  // obtaining the title to print
  console.log(data.title);
});
