#!/usr/bin/node
const request = require('request');
const process = require('process');
const url = process.argv[2];
const users = {};
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    for (let i = 0; i < todos.length; i++) {
      const todo = todos[i];
      if (String(todo.userId) in users && todo.completed === true) {
        users[String(todo.userId)] = users[String(todo.userId)] + 1;
      } else if (todo.completed === true) {
        users[String(todo.userId)] = 1;
      }
    }
    console.log(users);
  }
});
