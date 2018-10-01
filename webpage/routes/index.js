var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
var PotentialAnswer = mongoose.model('PotentialAnswer');

/* GET home page. */
router.get('/', function(req, res, next) {
  var array = PotentialAnswer.find({}, function(err, result){
    //TODO: add an err check here
    res.render('index', { title: result })
  });

});

module.exports = router;
