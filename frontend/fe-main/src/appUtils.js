import { consts } from "./consts.js"

/**
 * Checks for updates until one is detected and then sets updated page content.
 * @param {function} setCurrData currData setter
 */
export const getAndSetData = (setCurrData) => {
    fetch(consts.FILESYS_API_FQDN)
        .then(resp => resp.json())
        .then(respJson => setCurrData(respJson))
        .catch(err => console.error(err))
}

/**
 * Posts question's answer selection to feFilesys API. Then updates page content.
 * @param {string} respKey key of response choice
 * @param {string} respTxt text of response choice
 * @param {object} currData current page content
 * @param {function} setCurrData currData setter
 */
export const postAns = (respKey, respTxt, currData, setCurrData) => {
    const qAns = {
        "Question": currData.Question,
        "Selected_Response": {}
    }
    qAns["Selected_Response"][respKey] = respTxt
    const headers = {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(qAns)
    }

    // Post user selection.
    fetch(consts.FILESYS_API_FQDN, headers)
        .then(resp => {
            const status = resp.status
            // If data successfully posted, update page content.
            if (status === 200 || status === 304) {
                getAndSetData(setCurrData)
            } else {
                console.error(`Post gave response code ${status}.`)
            }
        })
}