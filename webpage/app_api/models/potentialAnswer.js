var mongoose = require('mongoose');

var potentialAnswerSchema = mongoose.Schema({
  text: String,
  url: String
},
{collection: 'sentencesWith42'}
);

mongoose.model('PotentialAnswer', potentialAnswerSchema);
