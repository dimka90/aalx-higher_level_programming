#!/usr/bin/node
/* This module make use of the file system api
*  to write content to a file
*/
const mod = require('fs');
// using the file system(fs) to open

mod.writeFile(process.argv[2], process.argv[3], 'utf8', (error, code) => {
  if (error) {
    console.log(error);
  }
});
