#!/usr/bin/node

function add (a, b) {
  const ans = a + b;
  return (ans);
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
const ans = add(a, b);
console.log(ans);
