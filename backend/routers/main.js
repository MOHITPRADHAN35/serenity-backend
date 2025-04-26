const express = require('express');
const app = express();
const journalRoute = require('./routes/journal');
app.use(express.json());
app.use('/journal', journalRoute);
