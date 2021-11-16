import { consts } from "./consts.js"

/**
 * Posts question's answer selection to feFilesys API.
 * @param respKey key of response choice
 * @param respTxt text of response choice
 */
export const postAns = (respKey, respTxt, currQTxt) => {
    const qAns = {
        "Question": currQTxt,
        "Selected_Response": {}
    }
    qAns["Selected_Response"][respKey] = respTxt

    fetch(consts.filesysApiPath, {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(qAns) 
    })
}