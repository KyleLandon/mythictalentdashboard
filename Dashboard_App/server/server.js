// api.js
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const bodyParser = require('body-parser');
const creatorsRouter = require('./api/creators'); // Import the creators routes

const app = express();
const port = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Connect to MongoDB
mongoose
  .connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    console.log('MongoDB connected');
  })
  .catch((err) => {
    console.error('MongoDB connection error:', err);
  });

// API Routes
app.use('/api/creators', creatorsRouter); // Mount the creators routes under /api/creators

// Start server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
