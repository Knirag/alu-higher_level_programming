#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    results.forEach(result => {
      result.characters.forEach(characterUrl => {
        if (characterUrl.includes('18')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
