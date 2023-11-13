#!/usr/bin/node
// Storing the values of command line arguments
const args = process.argv;
// checking  for the of the comand line arguments
if (args.length < 3) {
  console.log('No argument');
} else if (args.length > 2) {
  console.log(args[2]);
}
