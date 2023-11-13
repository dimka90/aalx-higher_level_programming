#!/usr/bin/node
// Storing the values of command line arguments
const args = process.argv;
// checking  for the of the comand line arguments
if (!args[2]) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
