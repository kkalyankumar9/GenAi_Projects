import React, { useState } from 'react';
import axios from 'axios';
import { Box, Button, Select } from '@chakra-ui/react';
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
              console.log(error);
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
              console.log(error);
            });

    }
  return (
    <Box m={4}>
    <form onSubmit={handleConvert}>
      <Select placeholder="Select Language" value={lan} onChange={(e) => setLang(e.target.value)}>
        <option value="javascript">JavaScript</option>
        <option value="java">Java</option>
        <option value="python">Python</option>
        <option value="c">C Language</option>
      </Select>

      <MonacoEditor
        width="800"
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

      <Button type='submit'>Convert</Button>
      <Button onClick={handleDebug}>Debug</Button>
    <Button onClick={handleQuality}>Check quality</Button>


    </form>
   

    <Box m={4}>
                {result.split('\n').map((line, index) => (
                    <Box key={index}>{line}</Box>
                ))}
            </Box>
  </Box>
  )
}

export default CodeConveter