import fs from 'fs';

import {constants} from "./constants.mjs"; // Get general constants of project

export const importCurrentQuestion = () => {
    var feBeFiles = fs.readdirSync(constants.BE_FE_PATH);
}

/**
   * Transmit question response to backend, via file-write.
   */
 export const exportQuestionResp = (questionResp) => {
    fs.writeFile(constants.feBe_path + "questionResp.json", JSON.stringify(questionResp), err => {

        // Checking for errors
        if (err) throw err;

        console.log("Done writing"); // Success
    });
}

// TODO
/**
 * Gets time of latest backend-to-frontend JSON transmission. Logs warning to console
 * if this time is greater than 10min since the last.
 *
 * File/string formats are YYYYMMDDhhmmssuuuuuu.json,
 * where YYYY is the four-digit year, MM is the two-digit month number,
 * DD is the two-digit day of the month, hh is the 24-hour representation of the hour
 * (e.g. 3 pm would be 15), mm is the two-digit minute, ss is the two-digit second,
 * and uuuuuu is the six-digit microsecond.
 *
 * @returns string of latest time
 */
 export const getLatestBeFeTime = (latestBeFeFeBeTime, setLatestBeFeTime) => {

    return 0.0
}

/**
 * @param now Date obj
 * @returns string of current time in format "YYYYMMDDhhmmss"
 */
 export const getCurrentTime = (now) => {
    var timeStr = String(now.getFullYear()); console.log(timeStr);
    timeStr += String(String(now.getMonth())); console.log(timeStr);
    timeStr += String(now.getDate()); console.log(timeStr);
    timeStr += String(now.getHours()); console.log(timeStr);
    timeStr += String(now.getMinutes()); console.log(timeStr);
    timeStr += String(now.getSeconds()); console.log(timeStr);
    return timeStr;
  }