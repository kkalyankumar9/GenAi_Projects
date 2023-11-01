import { Box, Heading, Input, Text, Button, VStack, Spinner, Flex } from '@chakra-ui/react'
import React, { useState } from 'react'
import axios from "axios"
const Translate = () => {
    
    const [text,setText]=useState("")
    const [convertLanguage,setConvertLanguage]=useState("")
    const [result,setResult]=useState("")
    const [loading,setLoading]=useState(false)
    const handleClickContentGen=async(e)=>{
        e.preventDefault()

        if(text!==""){
            setLoading(true)
            try {
        
                const response=await axios.post(`https://translate-vm1s.onrender.com/contentgen`,{text:text})
                setResult(response.data.contentGeneration)
                console.log(response.data.contentGeneration)
                setLoading(false)
        
        
                
            } catch (error) {
                console.log(error)
                
            }finally{
                setLoading(false)
            }

        }else{
            alert("Provide some Text")
            setLoading(false)
        }

   

    }
    const handleClickContentSummarize=async()=>{
        if(text!==""){
            setLoading(true)
            try {
        
                const response=await axios.post(`https://translate-vm1s.onrender.com/summary`,{text:text})
                setResult(response.data.summarize)
                console.log(response.data.summarize)
                setLoading(false)
                setText("")
        
                
            } catch (error) {
                console.log(error)
                setLoading(false)
                
            }finally{
                setLoading(false)
            }
        

        }else{
            alert("Provide some Text")
            setLoading(false)
        }
        
    }
    const handleClickContentTranslate=async()=>{
        if(text!==""&& convertLanguage!==""){
            setLoading(true)

            try {
        
                const response=await axios.post(`https://translate-vm1s.onrender.com/translate`,{text:text,language:convertLanguage})
                setResult(response.data.translate)
                console.log(response.data.translate)
                setConvertLanguage("")
                setText("")
                setLoading(false)
                
        
        
                
            } catch (error) {
                console.log(error)
                setLoading(false)
                
            }finally{
                setLoading(false)
            }
        

        }else{
            alert("Provide some Text")
            setLoading(false)

        }
    }

  return (
    <Box >

        <Heading  p={2} color={"violet"}>Content Generation and translator</Heading>
        <VStack bgColor={"white"} boxShadow=" rgba(99, 99, 99, 0.2) 0px 2px 8px 0px" w="500px"m={"auto"} p={5}>
      
        <Text
        as="textarea"
        placeholder="Enter text"
        h="200px"
        w="400px"
        overflowY="auto"
        borderWidth="1px"
        p={4}
        value={text}
        onChange={(e)=>setText(e.target.value)}

      />    
 
      <Input placeholder={"Enter language"} 
        w="300px"
        value={convertLanguage}
        onChange={(e)=>setConvertLanguage(e.target.value)}
        />
      <Button onClick={handleClickContentGen}>Generate</Button>
      <Flex justify={"space-between"} p={"5px"}>

      <Button onClick={handleClickContentSummarize}>Summarize</Button>
      <Button onClick={handleClickContentTranslate}ml={"5px"}>Translate</Button>
      </Flex>

      </VStack>
      <Box width={"600px"} bgColor={"gray.50"} m={"auto"} mt={2}p={5}>
        {!loading?<Box p={5} mt={"10px"}>{result}</Box>:<Spinner  thickness='4px'
  speed='0.65s'
  emptyColor='gray.200'
  color='blue.500'
  size='md'/> }
  {!result ? <Text> Generated data coming here..</Text> : ""}

  </Box>

    </Box>
  )
}

export default Translate