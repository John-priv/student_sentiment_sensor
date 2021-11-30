import { postAns } from "./appUtils.js"

export const GeneralSolution = (props) => {
    const [currData] = [props.currData]

    return (
        <div className='general-solution'>
            <div className='text-section'>
                <div className='solution-text'>{currData.Text}</div>
            </div>
            <div className='info-listings-section'>
                <ul>
                    {Object.keys(currData["Info Listings"]).map((lKey) => (
                        <li key={lKey}>
                            {console.log(currData["Info Listings"]["Link"])}
                            <a href={currData["Info Listings"][lKey]["Link"]}>{currData["Info Listings"][lKey]["Text"]}</a>
                        </li>
                    ))}
                </ul>
            </div>
            <div className='email-entry-section'>
                <form>
                    <label for="email-entry">If you would like to be sent these resources, feel free to enter your email:</label>
                    <input type="text" id="email-entry" name="email-entry"></input>
                    <input type="submit" value="Submit"></input>
                </form>
            </div>
        </div>
    )
}

export const GeneralQuestion = (props) => {
    const [currData, setCurrData] = [props.currData, props.setCurrData]

    return (
        <div className='general-question'>
            <div className='question-section'>
                <div className='question-text'>{currData.Text}</div>
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