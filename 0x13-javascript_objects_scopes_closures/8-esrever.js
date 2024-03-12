#!/usr/bin/node

exports.esrever = function (list) {
  const listsize = list.length;
  const newlist = [];
  for (let i = listsize - 1; i >= 0; i--) {
    newlist.push(list[i]);
  }
  return newlist;
};
