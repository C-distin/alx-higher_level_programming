#!/usr/bin/node
const Dict = require('./data/101-data').dict;

const sortDict = {};
for (let key in Dict) {
  if (sortDict[Dict[key]] === undefined) {
    sortDict[Dict[key]] = [];
  }
  sortDict[Dict[key]].push(key);
}
console.log(sortDict);
