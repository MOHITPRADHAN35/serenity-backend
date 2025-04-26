const express = require('express');
const router = express.Router();
const db = require('../firebase'); // import Firestore

router.post('/add-entry', async (req, res) => {
  try {
    const data = req.body;
    const response = await db.collection('journalEntries').add(data);
    res.status(200).send({ id: response.id });
  } catch (error) {
    res.status(500).send(error.message);
  }
});

module.exports = router;
