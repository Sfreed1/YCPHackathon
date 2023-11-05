const express = require('express');
const fs = require('fs');
const path = require('path');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.use(bodyParser.json());

app.post('/api/save-text', (req, res) => {
    // Define the directory where the files will be saved
    const directory = 'Desktop'; // Make sure this directory exists on your server

    // Generate a unique filename
    const filename = `webpage_${Date.now()}.txt`;

    // Define the full path for the file
    const filePath = path.join(directory, filename);

    // Write the text to a file
    fs.writeFile(filePath, req.body.text, (err) => {
        if (err) {
            console.error(err);
            res.status(500).send('Error writing file on server');
            return;
        }
        res.status(200).send('Text saved successfully as file');
    });
});

app.listen(port, () => console.log(`Server running on port ${port}`));
