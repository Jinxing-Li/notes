const Note = require('./Note');

var notes = [];

exports.update = exports.create = async function(key, title, body) {
     notes[key] = new Note(key, title. body);
     return notes[key];
}