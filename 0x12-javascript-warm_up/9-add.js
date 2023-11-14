#!/usr/bin/node

const args = process.argv;

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  console.log(a + b);
}

add(args[2], args[3]);
