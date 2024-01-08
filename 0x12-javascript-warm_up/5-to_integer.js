#!/usr/bin/node

const input = process.argv[2];

if (isNaN(input)) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(input));
}
