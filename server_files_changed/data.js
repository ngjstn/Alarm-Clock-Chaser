
// file parsing input
const fs = require('fs');

// express and router imports
var express = require("express");
var router = express.Router();

// get request handler that returns the json to the alarm clock buggy
router.get("/", function(req, res, next) {
    fs.readFile('../client/public/data.json', (err, json) => {
        let obj = JSON.parse(json);
        res.json(obj);
    });
    // res.send("API is working properly");
});

// get request handler that tests that the routing is correct
router.get("/test", function(req, res, next) {
    fs.readFile('../client/public/data.json', (err, json) => {
        let obj = JSON.parse(json);
        res.json(obj);
    });
    // res.send("API is working properly");
});

// post request that parses the user input and saves it to a json for the alarm clock buggy
router.post('/', function requestHandler(req, res) {
    let id1 = req.body.minute;
    let hour1 = req.body.hour;
    let song1 = req.body.song;
    console.log(id1 + "\n");
    console.log(hour1 + "\n");
    console.log(song1 + "\n");
    
    let data = {
        hour:hour1,
        minute:id1,
        song:song1
    }

    let json_new = JSON.stringify(data);


    fs.writeFile('../client/public/data.json', json_new, (err) => {
        if (err) throw err;
        console.log('Data written to data.json');
    });

    res.end();
});
module.exports = router;
