const express = require("express");
const bodyParser = require("body-parser");
const multer = require("multer");
var upload = multer();
var {PythonShell} = require('python-shell');

var app = express();
courses = [];

app.use(bodyParser.urlencoded({ extended: true })); 
app.use(express.static(__dirname + '/views'));
app.use(upload.array()); 

app.get('/', (req, res)=> {
    res.render("index.html");
});

app.post('/courses', function(req, res) {
    console.log(req.body.course);
    courses.push(req.body.course);
  });

function calculate(req, res) {
    var options = {
        args:
        [
        courses
        ]
    };
    PythonShell.run('igetccalculation.py', options, function (err, data) {
        if (err) {
            console.log("error");
            res.send(err);
        } else {
            console.log(data);
            res.send(data.toString())
        }
    });
}
  
app.get('/calculation', calculate);

app.listen(8080);