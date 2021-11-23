// Date string is formatted as YYYYMMDDhhmmsscc.

var express = require("express")
var router = express.Router()
const feFilesysApiUtils = require("./feFilesysApiUtils")
const sleep_ms = feFilesysApiUtils.sleep_ms
const getCurrTime = feFilesysApiUtils.getCurrTime
const getLatestBeFeTime = feFilesysApiUtils.getLatestBeFeTime
const getCurrData = feFilesysApiUtils.getCurrData
const filewriteQAns = feFilesysApiUtils.filewriteQAns

/**
 * Pass in placeholder latest transmission time to ensure that [1] the latest
 * or [2] any new BE-FE file's basename will be registered as the latest date.
 * The file "0000000000000000.json" should always exist in the
 * BE_FE_PATH_FROM_ROOTas a base case. 
 */
var latestBeFeTime = getLatestBeFeTime("0000000000000000", getCurrTime())
// The value of latestBeFeTime preceding an answer post req.
var formerLatestBeFeTime = "" // Should not initially match latestBeFeTime
var currData = getCurrData(latestBeFeTime) // Current page data

router.get("/", function (req, res, next) {
    // Ensure answer is up to date.
    while (latestBeFeTime === formerLatestBeFeTime) {
        latestBeFeTime = getLatestBeFeTime(latestBeFeTime, getCurrTime())
    }
    
    // while (!answerUpdated) {
    //     sleep_ms(50)
    // }

    currData = getCurrData(latestBeFeTime)
    var currData_json = JSON.parse(currData.toString())

    console.log("About to send.", currData_json)

    res.set({
        'Content-Type': 'application/json; charset=utf-8',
    })
    res.send(currData_json)

    console.log(req.headers)
})

router.post("/", function (req, res, next) {
    formerLatestBeFeTime = latestBeFeTime

    // answerUpdated = false
    filewriteQAns(req.body, latestBeFeTime)
    console.log("Received ", req.body)
    // answerUpdated = true
    res.send("Answer received.")
})

module.exports = router