const express=require("express");
const { contentRouter } = require("./Route/contentConvertor");
require('dotenv').config()

const app=express();
const PORT = process.env.PORT;
app.use(express.json());
app.use("/",contentRouter)


app.listen(PORT,()=>{
    console.log(`Server running at ${PORT}`)
})
