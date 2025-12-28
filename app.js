const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.status(200).send('Hello World!');
});

app.get('/health', (req, res) => {
  res.status(200).json({ status: 'UP' });
});

// Export the app for testing purposes
const server = app.listen(port, () => {
    console.log(`App listening at http://localhost:${port}`);
});

module.exports = server;
