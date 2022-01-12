const express = require('express');
const router = express.Router();

const User = require('../models/User');

router.get('/domaincost/:domain', async (req, res) => {
    //const domain = req.params.domain;
    //const pola = new User(req.body);
    const users = await User.aggregate([
      { $match : { domain : req.params.domain,} },
  ])
  let domaincost=0;
  users.forEach(user=>
    domaincost=domaincost+user.cost
  )
  
    try {
      //res.send(req.query.date);
      res.send({"Result":"Cost of "+domain+" domain:"+domaincost});
    } catch (error) {
      res.status(500).send(error);
    }
  });

router.get('/findByNameFirstNameDomain', async (req, res) => {
  // const users = await User.find({registrationDate : { $gte:req.query.date}}).count();
  const pola = req.body;
/*  const users = await User.aggregate([ // w mongo aggregate
    { $match : { $and:[{first_name : pola.first_name},{second_name : pola.second_name},{domain : pola.domain}] } },
    { $group: { _id: null, count: { $sum: 1 } } }
]) */
let users=await User.find({});
users=users.filter(user=>user.first_name==pola.first_name).filter(user=>user.second_name==pola.second_name).filter(user=>user.domain==pola.domain)
  try {
    //res.send(req.query.date);
    res.send({"Wynik":users});
  } catch (error) {
    res.status(500).send(error);
  }
});
//znalezienie wszystkich rekordow
router.get('/', async (req, res) => {
  const users = await User.find({});

  try {
    res.send(users);
  } catch (error) {
    res.status(500).send(error);
  }
});

router.post('/', async (req, res) => {
  const newUser = new User(req.body);

  try {
    await newUser.save();
    res.send(newUser);
  } catch (error) {
    res.status(500).send(error);
  }
});



router.delete('/:idUser', async (req, res) => {
  try {
    const deletedUser = await User.findByIdAndDelete(req.params.idUser);

    if (!deletedUser) res.status(404).send("No item found");
    res.status(200).send("udano");
  } catch (error) {
    res.status(500).send("blad:"+error);
  }
});

router.patch('/:idUser', async (req, res) => {
  try {
    await User.findByIdAndUpdate(req.params.idUser, req.body);
    await User.save();
    res.send(req.body);
  } catch (error) {
    res.status(500).send(error);
  }
});


module.exports = router;
