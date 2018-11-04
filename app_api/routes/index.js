var express = require('express');
var router = express.Router();

var ctrlAnswers = require('../controllers/potentialAnswerCtrl');

router.get('/', ctrlAnswers.getAllPotentialAnswers);

module.exports = router;
