#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    try {
      // Parse the JSON response
      const filmsData = JSON.parse(body);

      // Filter films where "Wedge Antilles" is present (character ID 18)
      const filmsWithWedge = filmsData.results.filter((film) => {
        return film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
      });

      // Print the number of movies where "Wedge Antilles" is present
      console.log(filmsWithWedge.length);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
