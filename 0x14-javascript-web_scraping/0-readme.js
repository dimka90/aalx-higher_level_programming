#!/usr/bin/node
/*
* this module performs a basic operation of open a
* file descriptor and reading the content of the file
* ===================================================
* it make use of callback function for error checking
*/
const mod = require('fs');

mod.readFile(process.argv[2], 'utf8', (error, code) => {
  if (error) {
    console.log(error);
  }
  console.log(code);
}

);
