#!/usr/bin/node
exports.converter = function (base) {
  function baseNum (num) {
    return num.toString(base);
  }
  return baseNum;
};
