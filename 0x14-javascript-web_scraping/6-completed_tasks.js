#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.log('Failed to fetch data.');
    return;
  }
  const tasks = JSON.parse(body);
  const tasksFinished = {};

  tasks.forEach((task) => {
    if (task.completed) {
      tasksFinished[task.userId] = (tasksFinished[task.userId] || 0) + 1;
    }
  });
  console.log(tasksFinished);
});
