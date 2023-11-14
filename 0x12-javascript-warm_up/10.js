#!/usr/bin/node
const args = process.argv;

function factorial(n) {
  n = parseInt(n);
  if (isNaN(n) || n < 0) {
    console.log("Please provide a non-negative integer.");
  } else if (n === 0) {
    console.log(1);
  } else {
    let result = n * factorial(n - 1);
    console.log(result);
  }
}

factorial(args[2]);
