#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nbOccurrences = 0;
  for (let l = 0; l < list.length; l++) {
    if (searchElement === list[l]) {
      nbOccurrences++;
    }
  }
  return nbOccurrences;
};
