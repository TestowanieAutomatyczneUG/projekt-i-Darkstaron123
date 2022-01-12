const { Schema, model } = require('mongoose');

const userSchema = new Schema({
    id:{type:Number,required:true},
    first_name: {
        type: String,
        required: true
    },
    second_name: {
        type: String,
        required: true
    },
    gender: {
        type: String,
        required: true
    },
    date: {
        type: String,
        required: true
    },
    time: {
        type: Date,
        required: true
    },
    domain: {
        type: String,
        required: true
    },
    cost: {
        type: Number,
        required: true,
        minimum:0
    },
    
}, {collection: 'kolokwium'});

module.exports = model('User', userSchema);