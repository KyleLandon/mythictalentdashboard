const express = require('express');
const Creator = require('../models/creators');
const router = express.Router();

router.post('/', async (req, res) => {
  const newCreator = new Creator(req.body);
  await newCreator.save();
  res.json(newCreator);
});

router.get('/', async (req, res) => {
  const creators = await Creator.find(req.query);
  res.json(creators);
});

router.put('/:id', async (req, res) => {
  const updatedCreator = await Creator.findByIdAndUpdate(req.params.id, req.body, { new: true });
  res.json(updatedCreator);
});

router.delete('/:id', async (req, res) => {
  await Creator.findByIdAndDelete(req.params.id);
  res.json({ message: 'Creator deleted' });
});

module.exports = router;
