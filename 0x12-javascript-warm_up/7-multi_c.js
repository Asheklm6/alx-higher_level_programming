#!/usr/bin/node

const arg = process.argv[2];

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = arg - 1; i >= 0; i--) {
    console.log('C is fun');
  }
}
