const express = require("express");
const app = express();

// Public test route (NO AUTH)
app.get("/api/health", (req, res) => {
  res.status(200).json({ ok: true });
});

// Protected honeypot route
app.get("/api/honeypot", (req, res) => {
  const apiKey = req.headers["x-api-key"];

  if (apiKey !== "GUVI123") {
    return res.status(401).json({
      error: "Unauthorized"
    });
  }

  res.status(200).json({
    status: "success",
    message: "Honeypot active"
  });
});

module.exports = app;