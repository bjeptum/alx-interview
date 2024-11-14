#!/usr/bin/node

const request = require('request');

// Get movie ID from cmd line argument
const movieId = process.argv[2];

// Create URL to get data for the movie
const url = `https://swapi.dev/api/films/${movieId}/`;

// Make HTTP request to the API to fetch movie data
request(url, function (error, response, body) {
  // If there’s an error, print it
  if (error) {
    console.log('Error:', error);
    return;
  }
  // If the request is successful get a valid movie response
  if (response.statusCode === 200) {
    // Convert response body into a JavaScript object
    const movie = JSON.parse(body);
    // Get the list of character URLs from the movie data
    const characters = movie.characters;

    // For each character URL, make a request to get the character's details
    characters.forEach(characterUrl => {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.log('Error:', error);
        } else if (response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name); // Print the character's name
        }
      });
    });
  } else {
    // If the movie request fails, print an error message
    console.log('Failed to fetch movie data');
  }
});
