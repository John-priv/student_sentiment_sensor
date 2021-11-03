import React, { useState } from 'react'
import fs from 'fs';

import {getCurrentTime, getLatestBeFeTime, exportQuestionResp} from "./utils.mjs";

export default function App (props) {
  /**
   * Reacts to button click event.
   * @param {string} respOption 
   * @param {int} index 
   */
  const handleRespButtonClick = (respOption, index) => {
    //exportQuestionResp(respOption);
    console.log('success')
  }

    /**
   * Initialize local vars.
   */
     var questionResp = {
      Question: '',
      Selected_Response: {}
    }
  const dateTruncLength = "YYYYMMDDhhmmss".length; // Time to precision of 1s
  const currentQ_responses = Object.values(props.currentQ.Responses);

  // Initialize each state var and its respective setter function.
  const [currentQuestion, setCurrentQuestion] = useState(0)
  const [score, setScore] = useState(0)
  const [showScore, setShowScore] = useState(false)
  /**
   * Time, and setter, of [1] latest frontend-to-backend JSON transmission, unless this
   * is the app's first render in which case it is [2] the latest backend-to-frontend
   * JSON transmission.
   */
  const [latestFeBeTime, setLatestFeBeTime] = useState(getLatestBeFeTime())


  /**
   * Top-level construct.
   */
  return (
    <div className='app'>
      <div className='question-section'>
        <div className='question-text'>{props.currentQ.Question}</div>
      </div>
      <div className='answer-section'>
        {currentQ_responses.map((respOption, index) => (
          <button onClick={() => handleRespButtonClick(respOption, index)}>
            {respOption}
          </button>
        ))}
      </div>
    </div>
  )
}