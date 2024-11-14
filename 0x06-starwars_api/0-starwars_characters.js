#!/usr/bin/node

const request = require('request');

// Get movie ID from cmd line argument
const movieId = process.argv[2];

// Create URL to get data for the movie
const url = `https://swapi.dev/api/films/${movieId}/`;

// Function to make HTTP request to fetch data and return a promise
function fetchData (url) {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error) {
        reject(error);
      } else if (response.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(new Error('Failed to fetch data'));
      }
    });
  });
}

async function printCharacters () {
  try {
    // Fetch movie data
    const movie = await fetchData(url);

    // Get the list of character URLs from the movie data
    const characters = movie.characters;

    // For each character URL, get character data and print their name in order
    for (const characterUrl of characters) {
      const character = await fetchData(characterUrl);
      console.log(character.name); // Print the character's name
    }
  } catch (error) {
    console.log('Error:', error);
  }
}

// Run the function to print characters
printCharacters();
