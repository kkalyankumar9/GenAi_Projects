import React, { useState } from 'react';
import axios from 'axios';
import { Box, Button,Text, Flex, Heading, Select } from '@chakra-ui/react';
import MonacoEditor from 'react-monaco-editor';
import { Spinner } from '@chakra-ui/react'
const CodeConveter = () => {
    const [code, setCode] = useState('');
    const [lan, setLang] = useState('');
    const [result, setResult] = useState('');
    
  
    const handleConvert = (e) => {
        e.preventDefault();
        if(code==="" && lan===""){
        alert("Please give some code and select convert language")
        }else{
      
      axios.post(`https://codeconverter-server.onrender.com/convert`, { code: code, language: lan },{  headers: {
        'Content-Type': 'application/json',
    
      }},)
        .then((response) => {
            setResult(response.data.convertCoding);
          console.log(response.data.convertCoding)
        })
        .catch((error) => {
          console.log(error);
        });
    }
    };
    const handleDebug=()=>{
        axios.post(`https://codeconverter-server.onrender.com/debug`, { code: code},{  headers: {
            'Content-Type': 'application/json',
        
          }},)
            .then((response) => {
                setResult(response.data.debuggedCode);
              console.log(response.data.debuggedCode)
            })
            .catch((error) => {
              console.error("An error occurred:", error);
              // Display an error message to the user
          });

    }
    const handleQuality=()=>{
        axios.post(`https://codeconverter-server.onrender.com/check-quality`, { code: code},{  headers: {
            'Content-Type': 'application/json',
        
          }},)
            .then((response) => {
                setResult(response.data.qualityEvaluation);
              console.log(response.data.qualityEvaluation)
            })
            .catch((error) => {
              console.error("An error occurred:", error);

          });

    }
  return (
    <Box >
    <Heading color={"teal"}>Code Convertor</Heading>
    <Flex  direction={['column', 'row']} wrap={"wrap"} textAlign={"center"} justify={"center"}     >

    <Box m={4} textAlign={"center"} >
    <form onSubmit={handleConvert} p={5}  >
      <Select placeholder="Select Language" value={lan} onChange={(e) => setLang(e.target.value)} bgColor={"white"} w={"200px"} textAlign={"center"} p={2}>
        <option value="javascript">JavaScript</option>
        <option value="java">Java</option>
        <option value="python">Python</option>
        <option value="c">C Language</option>
      </Select>

      <MonacoEditor
        width="700"
        height="400"
      
        language="javascript"
        theme="vs-dark"
        value={code}
        options={{
          selectOnLineNumbers: true,
          roundedSelection: false,
          cursorStyle: 'line',
          automaticLayout: true,
          
        }}
        onChange={(value) => setCode(value)}
      />
      <Flex p={5} ml={4}  direction={['column', 'row']} justifyContent={"space-around"} >

      <Button  ml={4} type='submit'>Convert</Button>
   
    
    <Button ml={4} onClick={handleDebug}>Debug</Button>
    <Button  ml={4} onClick={handleQuality}>Check quality</Button>
    </Flex>
    </form>
    </Box>

    <Box mt={8}  p={4}  bgColor={"white"}w={"500px"} boxShadow=" rgba(0, 0, 0, 0.16) 0px 1px 4px">
                {result.split('\n').map((line, index) => (
                    <Box key={index} textAlign={"left"} w={"100%"} p={1}>{line}</Box>
                ))}
              
            </Box>

  </Flex>
  </Box>
  )
}

export default CodeConveter