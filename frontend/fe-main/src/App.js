import { useEffect, useState } from 'react'
import { GeneralSolution, GeneralQuestion } from './components.js'
import { getAndSetData } from "./appUtils.js"

function App() {

  const [currData, setCurrData] = useState({
    "Prompt type": "Question", // Defaults to a (blank) general question.
    "Text": "",
    "Responses": {}
  })
  const promptsDict = {
    "Question": GeneralQuestion,
    "Solution": GeneralSolution,
  }

  useEffect(() => {
    getAndSetData(setCurrData)
  }, [])

  const CurrPrompt = promptsDict[currData["Prompt type"]]
  const props = {currData: currData, setCurrData: setCurrData}
  return (
    <CurrPrompt {...props} />
  )
}

export default App
