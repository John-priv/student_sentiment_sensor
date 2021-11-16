var express = require("express")
var router = express.Router()
const feFilesysApiUtils = require("./feFilesysApiUtils")
const getCurrentTime = feFilesysApiUtils.getCurrentTime
const getLatestBeFeTime = feFilesysApiUtils.getLatestBeFeTime
const getCurrQ = feFilesysApiUtils.getCurrQ
const filewriteQAns = feFilesysApiUtils.filewriteQAns

// Date string will be formatted as YYYYMMDDhhmmsscc
var latestBeFeTime = getLatestBeFeTime("0000000000000000", getCurrentTime())
var currQ = getCurrQ(latestBeFeTime)

router.get("/", function (req, res, next) {
    latestBeFeTime = getLatestBeFeTime(latestBeFeTime, getCurrentTime())
    currQ = getCurrQ(latestBeFeTime)
    var currQ_json = JSON.parse(currQ.toString())
    console.log(currQ_json)

    res.set({
        'Content-Type': 'application/json; charset=utf-8',
    })
    res.send(currQ)
})

router.post("/", function (req, res, next) {
    filewriteQAns(req.body, latestBeFeTime)
})

module.exports = router