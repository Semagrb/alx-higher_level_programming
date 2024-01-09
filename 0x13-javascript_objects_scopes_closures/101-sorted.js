#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};

valsUniq.forEach(value => {
 const list = totalist.filter(entry => entry[1] === value).map(entry => entry[0]);
 newDict[value] = list;
});

console.log(newDict);
