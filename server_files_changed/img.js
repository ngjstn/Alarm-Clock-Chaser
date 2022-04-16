// file parser imports
const fs = require('fs');

// express and router imports
var express = require("express");
var router = express.Router();

// get request handler that returns the img
router.get("/", function(req, res, next) {
    fs.readFile('../client/public/img.json', (err, json) => {
        let obj = JSON.parse(json);
        res.json(obj);
    });
});

// test get request handler that ensures the api works
router.get("/test", function(req, res, next) {
    res.send("API is working properly");
});


// post request handler that takes the user's input image and saves it
router.post('/', function requestHandler(req, res) {
    let url = req.body.url;  // url of the image
    let time = req.body.time;  // time that the user stopped
    
    let data = {  // json data creation
        url:url,
        time:time
    }

    let json_new = JSON.stringify(data);   

    // writing the json data to the img file
    fs.writeFile('../client/public/img.json', json_new, (err) => {
        if (err) throw err;
        console.log('Data written to img');
    });

    res.end();
});
module.exports = router;
