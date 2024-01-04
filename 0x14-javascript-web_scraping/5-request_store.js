#!/usr/bin/node
// a  script that gets the contents of a webpage and stores it in a file
const request = require('request');
// file system for writing to a  file
const fs = require('fs');
// getting api url name from the terminal
const apiUrl = process.argv[2];
// calling the request method on the url
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  // call the file system to write to a fiel
  fs.writeFile(process.argv[3], body, 'utf8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
