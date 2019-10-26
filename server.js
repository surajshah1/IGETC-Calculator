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

