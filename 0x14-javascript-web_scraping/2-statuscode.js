#!/usr/bin/node
// A  script that display the status code of a GET request
const request = require('request');

request(process.argv[2], (error, response) => {
  if (error) {
    console.log('code: 404');
  } else {
    console.log('code: ' + response.statusCode);
  }
}
);
