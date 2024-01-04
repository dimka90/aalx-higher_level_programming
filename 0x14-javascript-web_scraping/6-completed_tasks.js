#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from command line arguments

// Make a GET request to the Todo API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    try {
      // Parse the JSON response
      const todosData = JSON.parse(body);

      // Filter completed tasks
      const completedTasks = todosData.filter(todo => todo.completed);

      // Count completed tasks for each user ID
      const completedTasksByUser = completedTasks.reduce((result, todo) => {
        const userId = todo.userId.toString();
        result[userId] = (result[userId] || 0) + 1;
        return result;
      }, {});

      // Print the result
      console.log(completedTasksByUser);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
