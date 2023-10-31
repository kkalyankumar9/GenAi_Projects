const express=require("express");
const contentRouter=express.Router()
const axios=require("axios")
contentRouter.post("/contentgen",async(req,res)=>{
    const {text}=req.body
    
    try {
        const requestbody={
            "model": "gpt-3.5-turbo",
          
            "messages": [
                {
                    "role": "user", 
                    "content": `Summarize the provided ${text} `
                }
            ],
            "temperature": 0.7
    
        }
     const response= await axios.post("https://api.openai.com/v1/chat/completions",requestbody,
           {headers:{
                "Content-Type": "application/json",
                Authorization: `Bearer ${process.env.API_KEY}`
            }}
            )
        const contentGeneration=response.data.choices[0].message.content
        res.json({contentGeneration})
        console.log(contentGeneration)

        
    } catch (error) {
        res.status(400).send({"error":error})
    }
})
module.exports={contentRouter}