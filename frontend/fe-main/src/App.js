import { useEffect, useState } from 'react'
import {postAns} from "./appUtils.js"
import {consts} from "./consts.js"

function App() {                    
  const [currQ, setCurrQ] = useState({
    "Question": "",
    "Responses": {}
  })

  useEffect(() => {
    const setData = () => {
      fetch(consts.filesysApiPath)
        .then(resp => resp.json())
        .then(respJson => {setCurrQ(respJson)})
        .catch(err => { console.error(err) })
    }
    setData()
    const intervalId = setInterval(() => setData(), 5 * 1000)
    return () => {
      clearInterval(intervalId)
    }
  }, [])


  return (
    <div className='app'>
      <div className='question-section'>
        <div className='question-text'>{currQ.Question}</div>
      </div>
      <div className='answer-section'>
        {Object.keys(currQ.Responses).map((respKey) => (
          <button key={respKey} onClick={() => postAns(respKey, currQ.Responses[respKey], currQ.Question)}>
            {currQ.Responses[respKey]}
          </button>
        ))}
      </div>
    </div>
  )
}

export default App
