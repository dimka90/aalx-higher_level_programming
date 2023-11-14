#!/usr/bin/node

const args = process.argv;

const parsedInt = parseInt(args[2]);

if (isNaN(parsedInt)) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= args[2]; i++) {
    for (let j = 1; j <= args[2]; j++) {
      process.stdout.write('x');
    }
    console.log();
  }
}
