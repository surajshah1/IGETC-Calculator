<<<<<<< HEAD
/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


const express = require('express')
const react = require("react");
const dom = require("react-dom");
const App = require('App');

app.use(bodyParser.urlencoded({ extended: false }));

const server = express();

server.use('/assets', express.static('assets'));

server.get('/', (req, res) => {
  const appString = renderToString(<App />);

  res.send(template({
    body: appString,
    title: 'Hello World from the server'
  }));
});



server.listen(8000, () => {
    console.log("running on port 8000");
});

=======
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
        pythonOptions: ['-u'],
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
            //res.send(data.toString())
        }
    });

}
  
app.get('/calculation', calculate);

app.listen(8080);
>>>>>>> 0a3340e... initial changes
