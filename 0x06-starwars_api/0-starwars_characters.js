#!/usr/bin/node
// Script that prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”  
// Display one character name by line in the same order of the list “characters” in the /films/ endpoint
// You must use the Star wars API https://swapi-api.alx-tools.com/api/
// You must use the request module


const request = require('request');

async function getCharacterNames(movieId) {
  const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  const filmData = await new Promise((resolve, reject) => {
    request(filmUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });

  const characterUrls = filmData.characters;
  const characterNames = [];

  for (const characterUrl of characterUrls) {
    const characterData = await new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });

    characterNames.push(characterData.name);
  }

  return characterNames;
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as a command-line argument.');
} else {
  getCharacterNames(movieId)
    .then(names => {
      if (names.length === 0) {
        console.log('No characters found for the given Movie ID.');
      } else {
        names.forEach(name => console.log(name));
      }
    })
    .catch(error => {
      console.error('An error occurred:', error);
    });
}
