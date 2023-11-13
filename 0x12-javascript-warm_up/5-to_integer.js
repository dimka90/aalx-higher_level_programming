#!/usr/bin/node

const args = process.argv;

const parsedInt = parseInt(args[2]);

if (!args[2] || isNaN(parsedInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parsedInt}`);
}
