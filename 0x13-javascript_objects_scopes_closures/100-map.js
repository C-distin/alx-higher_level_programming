#!/usr/bin/node
const List = require('./data/100-data.js').list;
console.log(List);

const mapList = List.map((index, item) => index * item);
console.log(mapList);
