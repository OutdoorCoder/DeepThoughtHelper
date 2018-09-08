var mongoose = require('mongoose');
var PotentialAnswer = mongoose.model('PotentialAnswer');

module.exports.getAllPotentialAnswers = function(req, res){

  var array = PotentialAnswer.find({}, function(err, result){
    //TODO: add an err check here
    res.send(result);
  });
}
