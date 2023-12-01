#!/usr/bin/node

function largest()
{
let first = process.argv[2];
let last = process.argv[process.argv.length - 1];
let array = process.argv.slice(2);

if ((!process.argv[2]) || (process.argv.length === 3)) {
console.log(0);
}
else{
for (let i = 0 ; i < array.length; i++)
{
let large = parseInt(array[0]);
let value;
if (parseInt(array[i]) >= large){
large = parseInt(array[i]);
value = large;
//array.pop(large);
}
console.log(value);
console.log(array);
}
}
}
largest();
