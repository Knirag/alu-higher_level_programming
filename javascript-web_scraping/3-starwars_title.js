#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + process.argv[2], function (error, response, body) {
  // url + process.argv[2] is same as `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`
  console.log(error || JSON.parse(body).title);
});
