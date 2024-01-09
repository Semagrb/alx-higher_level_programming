#!/usr/bin/node
const { dict } = require('./101-data');

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const val of valsUniq) {
 const list = totalist.filter(([key, value]) => value === val).map(([key]) => key);
 newDict[val] = list;
}
console.log(newDict);
