const express = require("express");
const fetch = require("node-fetch");
const path = require("path");

const app = express();
const PORT = 3000;

// serve static files (index.html, style.css, script.js)
app.use(express.static(path.join(__dirname)));

// API proxy -> fetch data from Flask backend
app.get("/data", async (req, res) => {
  try {
    const response = await fetch("http://localhost:8000/api");
    const json = await response.json();
    res.json(json);
  } catch (error) {
    res.status(500).json({ error: "Failed to fetch backend" });
  }
});

app.listen(PORT, "0.0.0.0", () => {
  console.log(`Frontend running at http://localhost:${PORT}`);
});
