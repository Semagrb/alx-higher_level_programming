#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const second = Math.max(...process.argv.slice(2).map(Number));
  console.log(second);
}
