const express = require('express');
const axios = require('axios');
const cors=require("cors")
require('dotenv').config();

const app = express();
app.use(cors())
app.use(express.json());
const PORT = process.env.PORT||8000;



app.post("/get", async (req, res) => {
  try {
    const { keyword } = req.body;
    const { type } = req.query;

    if (!keyword) {
      return res.status(400).json({ error: "keyword is missing" });
    }
    if (!type) {
      return res.status(400).json({ error: "type is missing" });
    }

    const requestBody = {
      model: "gpt-3.5-turbo",
      messages: [
        {
          role: "user",
          content: `create ${type} on ${keyword}`,
        },
      ],
      max_tokens: 100,
    };

    const response = await axios.post(
      "https://api.openai.com/v1/chat/completions",
      requestBody,
      {
        headers: {
          Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
          "Content-Type": "application/json",
        },
      }
    );

    const data = response.data;
    const result = data.choices[0].message.content;
    console.log(result)

    res.json({ result });
  } catch (error) {
    console.error("Error:", error.message);
    res.status(500).json({ error: "Something went wrong" });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
