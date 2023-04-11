#!/usr/bin/node

const firstArg = process.argv[2];
const sym = 'X';

if (isNaN(firstArg)) {
  console.log('Missing size');
} else {
  for (let j = 1; j <= firstArg; j++) {
    console.log(sym.repeat(firstArg));
  }
}
