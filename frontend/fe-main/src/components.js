import { getTextSubmission, postAns } from "./appUtils.js"

export const GeneralSolution = (props) => {
    const [currData, setCurrData] = [props.currData, props.setCurrData]

    return (
        <div className='general-solution'>
            <div className='text-section'>
                <div className='solution-text'>{currData.Text}</div>
            </div>
            <div className='info-listings-section'>
                <ul>
                    {Object.keys(currData["Info Listings"]).map((lKey) => (
                        <li key={lKey}>
                            <a href={currData["Info Listings"][lKey]["Link"]}>{currData["Info Listings"][lKey]["Text"]}</a>
                        </li>
                    ))}
                </ul>
            </div>
            <div className='email-entry-section'>
                <form name="email-form">
                    <label htmlFor="email-entry">If you would like to be sent these resources, feel free to enter your email:</label><br></br><br></br>
                    <input type="email" id="email-entry-1" name="email-entry" placeholder="Email address"></input>
                    <input type="submit" value="Submit" onClick={() => postAns("emailTrue", document.forms['email-form'].elements[0].value, currData, setCurrData)}></input>
                </form>
            </div>
            <div>
            <br></br><br></br><br></br>
                <button onClick={() => postAns("emailFalse", "", currData, setCurrData)}>
                    Done with session
                </button>
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