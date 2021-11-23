import { useEffect, useState } from 'react'
import { getAndSetData, postAns } from "./appUtils.js"

function App() {

  const [currData, setCurrData] = useState({
    "Question": "",
    "Responses": {}
  })

  useEffect(() => {
    getAndSetData(setCurrData)
  }, [])


  return (
    <div className='app'>
      <div className='question-section'>
        <div className='question-text'>{currData.Question}</div>
      </div>
      <div className='answer-section'>
        {Object.keys(currData.Responses).map((respKey) => (
          <button key={respKey} onClick={() => postAns(respKey, currData.Responses[respKey], currData, setCurrData)}>
            {currData.Responses[respKey]}
          </button>
        ))}
      </div>
    </div>
  )
}

export default App
