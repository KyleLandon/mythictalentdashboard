const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const apiRoutes = require('./routes/api');
const app = express();

require("dotenv").config();
require('./db');


app.use(cors());
app.use(express.json());

app.use('/api/creators', apiRoutes);

app.listen(3001, () => {
  console.log('Server running on http://localhost:3001/');
});
