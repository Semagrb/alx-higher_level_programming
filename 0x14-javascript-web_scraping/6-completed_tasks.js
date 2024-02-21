#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    let completedTasksCount = 0;

    for (const task of tasks) {
      if (task.completed) {
        completedTasksCount++;
      }
    }

    console.log(completedTasksCount);
  } else {
    console.error('An error occurred. Status code: ' + response.statusCode);
  }
});
