const express = require('express');
const mongoose = require('mongoose');
const jwt = require('jsonwebtoken');
const User = mongoose.model('User');
const requireAuth = require('../middlewares/requireAuth');

const router = express.Router();

router.post('/signup', async (req, res) => {
  const { email, password } = req.body;

  try {
    const user = new User({ email, password });
    await user.save();

    const token = jwt.sign({ userId: user._id }, 'MY_SECRET_KEY');
    res.send({ token });
  } catch (err) {
    return res.status(422).send(err.message);
  }
});

router.post('/login', async (req, res) => {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(422).send({ error: 'Must provide email and password' });
  }

  const user = await User.findOne({ email });
  if (!user) {
    return res.status(422).send({ error: 'Invalid password or email' });
  }

  try {
    await user.comparePassword(password);
    const token = jwt.sign({ userId: user._id }, 'MY_SECRET_KEY');
    if (!user.fName){
      res.send({ token });
    } else {
      res.send({ 
        token,
        email: user.email,
        fName: user.fName,
        lName: user.lName,
        gender: user.gender,
        pNumber: user.pNumber,
        city: user.city,
        dob: user.dob
       });
    }

  } catch (err) {
    return res.status(422).send({ error: 'Invalid password or email' });
  }
});

router.put('/profile', requireAuth, async (req, res) => {

  const filter = { _id: req.user._id };
  const updateDocument = {
   $set: {
    fName: req.body.fName,
    lName: req.body.lName,
    gender: req.body.gender,
    pNumber: req.body.pNumber,
    city: req.body.city,
    dob: req.body.dob,
   },
  };


  try {
    await User.updateOne(filter, updateDocument);
    res.send({
      email: req.user.email,
      fName: req.body.fName,
      lName: req.body.lName,
      gender: req.body.gender,
      pNumber: req.body.pNumber,
      city: req.body.city,
      dob: req.body.dob
    });
  } catch (err) {
    return res.status(422).send(err.message);
  }

  /*
  console.log(req);
  const id = req.user._id;
  console.log(id);
  const fName = req.body.fName;
  console.log(fName);
   try{
    const user = await user.findOne({ email });
    console.log(user);
  } catch (err) {
    console.log(err);
  }

  try {
    await User.findOneAndUpdate({ id }, { fName });
    res.status(200).send('Success!');
  } catch (err) {
    return res.status(422).send(err.message);
  }
  */
});




// router.get('/profile', requireAuth, async (req, res) => {
//   if (!req.user.fName) {
//     return res.status(404).send({ error: 'You have to initialize your profile first!' }); }

//     res.send({
//       email: req.user.email,
//       fName: req.user.fName,
//       lName: req.user.lName,
//       gender: req.user.gender,
//       pNumber: req.user.pNumber,
//       city: req.user.city,
//       dob: req.user.dob
//     });
// });

module.exports = router;