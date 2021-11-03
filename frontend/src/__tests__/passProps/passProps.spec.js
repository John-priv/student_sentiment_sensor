// External deps
import React from "react";
import ReactDOM from "react-dom";

// Project-specific deps
import "../index.css";
import App from "../../App"; // Top-level component to be rendered
import {constants} from "../constants.mjs"; // Get general constants of project

describe("Pass props properly", () => {
    test("Check each props mapping.", () => {
        const root = document.createElement("div");
        var props = {
            now: new Date(), // Current date and time
            }
        ReactDOM.render(<App {...props}/>, root);
        expect(App).toHaveBeenCalledWith(props);
    });
  });