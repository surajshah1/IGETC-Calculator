/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


const express = require('express')

var app = express();



const pdftotext = require('node-pdftotext');
let options = { pdfPath: "/Users/sudhu/NetBeansProjects/IGETCCalculator/igetcplanner.pdf", layout: true, first: 3 };

var text = pdftotext(options, err => {
    if (err) {
        console.log(err);
    }
    else {
        console.log('converted to txt');
    }
});
app.get('/', (req, res) => {
    console.log(text);
    res.send("Igetc Calculator");
    
});


app.listen(8000, () => {
    console.log("running on port 8000");
});