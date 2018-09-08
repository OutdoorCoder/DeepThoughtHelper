var express = require('express');
var router = express.Router();

var crtlAnswers = require('../controllers/potentialAnswerCtrl');

router.get('/', ctrlAnswers.getAllPotentialAnswers);

/* GET home page. */
//router.get('/', function(req, res, next) {
  //res.render('index', { title: 'Express' });
//});

module.exports = router;
