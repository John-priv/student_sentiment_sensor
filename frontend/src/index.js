/**
 * The base script, to be run on Node.js by the backend.
 */


// External deps
import React from "react";
import ReactDOM from "react-dom";

// Project-specific deps
import "./index.css";
import App from "./App"; // Top-level component to be rendered
import {constants} from "./constants.mjs"; // Get general constants of project
import {getCurrentTime, getLatestBeFeTime} from "./utils.mjs";


var now = new Date(); // Current date and time
var currentQ = {
  "Question": "question resp",
  "Responses": {
    "1001": "Sports",
    "1002": "Arts",
    "1003": "School",
    "1004": "Fitness",
    "1005": "Food"
  }
};

console.log(getCurrentTime(now));



var props = {
  "currentQ": currentQ,
  }

ReactDOM.render(
  <React.StrictMode>
    <App {...props}/>
  </React.StrictMode>,
  document.getElementById("root")
);