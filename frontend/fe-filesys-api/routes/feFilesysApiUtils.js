const fs = require('fs')
const path = require('path')
const consts = require("../consts.js")

module.exports = {

    /**
     * Last 2 places, the centiseconds, will always be 0.
     * @returns string of current time in format "YYYYMMDDhhmmssuuuuuu"
     */
    getCurrTime: () => {
        var now = new Date()
        var timeStr = String(now.getFullYear())
            + ("0" + String(now.getMonth() + 1)).slice(-2)
            + ("0" + String(now.getDate())).slice(-2)
            + ("0" + String(now.getHours())).slice(-2)
            + ("0" + String(now.getMinutes())).slice(-2)
            + ("0" + String(now.getSeconds())).slice(-2)
            + "00"
        return timeStr
    },

    /**
     * Gets time of latest backend-to-frontend JSON transmission, updating the latestBeFeFeBeTime state variable in the process.
     * @param {string} formerLatestTime 
     * @param {string} currTime 
     * @returns string of latest time
     */
    getLatestBeFeTime: (formerLatestTime, currTime) => {
        const parseInt10DateStr = (dateStr) => {
            const dateStrLen = "YYYYMMDDhhmmsscc".length
            const numDigFront = 8
            const numDigBack = dateStrLen - numDigFront // 8
            const front = dateStr.slice(0, numDigFront)
            const back = dateStr.slice(-numDigBack)
            const frontNumE_numDigBack = parseInt(front, 10) * Math.pow(10, numDigBack)
            const backNum = parseInt(back, 10)
            return frontNumE_numDigBack + backNum
        }

        if (typeof (formerLatestTime) != "string" || typeof (currTime) != "string") {
            throw new Error("formerLatestTime must be of type 'string'.")
        }
        const dateStrLen = "YYYYMMDDhhmmsscc".length
        const formerLatestTime_num = parseInt10DateStr(formerLatestTime)


        // Convert array of file names into basenames as YYYYMMDDhhmmsscc-formatted numbers
        const feBeFilesArray = fs.readdirSync(path.resolve(__dirname, consts.BE_FE_PATH_FROM_ROOT))
            .filter(filename => filename.includes(".json"))
        const feBeFileBasenames = feBeFilesArray.map(fileName => fileName.substring(0, dateStrLen))
        const feBeFileBasenames_num = feBeFileBasenames.map(fileBasename => parseInt(fileBasename, 10))

        const whichOfTheseIsMax = feBeFileBasenames_num.concat(formerLatestTime_num)
        const newLatestTime = Math.max(...whichOfTheseIsMax)

        return newLatestTime.toString()
    },

    /**
     * Retrieves current question from file of latest frontend-backend (FE-BE) transmission.
     * @param {string} latestBeFeFeBeTime latest time of BE-FE transmission
     * @returns current page data, to be displayed to the user
     */
    getCurrData: (latestBeFeFeBeTime) => {
        var qPath = consts.BE_FE_PATH_FROM_ROOT
            + latestBeFeFeBeTime
            + ".json"
        return fs.readFileSync(path.resolve(__dirname, qPath))
    },

    /**
     * Transmit question response to backend via file-write.
     * @param {string} qAns user answer
     * @param {string} fileBasename basename of json file
     */
    filewriteQAns: (qAns, fileBasename) => {
        fs.writeFile(path.resolve(__dirname,
            consts.FE_BE_PATH_FROM_ROOT,
            fileBasename + ".json"),
            JSON.stringify(qAns),
            err => { if (err) throw err })
    },

    /**
     * Helper for waiting.
     * @param {number} interval_ms time to wait in ms
     */
    sleep_ms: (interval_ms) => {
        var tStart_ms = new Date().getTime();
        while (new Date() < tStart_ms + interval_ms) { }
    },
}