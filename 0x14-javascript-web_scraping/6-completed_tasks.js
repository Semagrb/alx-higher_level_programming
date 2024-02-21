#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const completedTasks = {};
    const tasks = JSON.parse(body);
    
    for (const task of tasks) {
      if (task.completed === true) {
        if (completedTasks[task.userId] === undefined) {
          completedTasks[task.userId] = 1;
        } else {
          completedTasks[task.userId]++;
        }
      }
    }
    
    console.log(completedTasks);
  } else {
    console.error('An error occurred. Status code: ' + response.statusCode);
  }
});
