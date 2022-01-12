const express = require('express');
const app = express();
app.use(express.json());





const MongoClient = require('mongodb').MongoClient;
const fs = require('fs');
const client = new MongoClient('mongodb://localhost:27017', { useUnifiedTopology:true });

client.connect(function(err) {
    const db = client.db('kolokwium');
    const data = fs.readFileSync('data.json');
    const docs = JSON.parse(data.toString());
    db.collection('kolokwium')
        .insertMany(docs, function(err, result) {
            if (err) throw err;
            console.log('ilosc objektow:', result.insertedCount);
            client.close();
    });
})