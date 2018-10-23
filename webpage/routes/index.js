var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
var PotentialAnswer = mongoose.model('PotentialAnswer');

/* GET home page. */
router.get('/', function(req, res, next) {
  var array = PotentialAnswer.find({}).sort({_id: -1}).exec(function(err, result){
    //TODO: add an err check here
    res.render('index', { potentialAnswer: result })
  });

});

module.exports = router;
