#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the provided API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  // Parse the response body into JSON format
  const todos = JSON.parse(body);

  // Create an object to store the number of tasks completed by each user ID
  const completedTasksByUserId = {};

  // Loop through the todos and count completed tasks for each user ID
  todos.forEach(todo => {
    if (todo.completed) {
      completedTasksByUserId[todo.userId] = (completedTasksByUserId[todo.userId] || 0) + 1;
    }
  });

  // Print the number of completed tasks for each user ID
  Object.keys(completedTasksByUserId).forEach(userId => {
    console.log(`User ID ${userId}: ${completedTasksByUserId[userId]} completed tasks`);
  });
});
