import React, { useState } from 'react';
import axios from 'axios';
import { Box, Button, Select } from '@chakra-ui/react';
import MonacoEditor from 'react-monaco-editor';

const Converter = () => {
  const [code, setCode] = useState('');
  const [lan, setLang] = useState('');
  const [conv, setConv] = useState('');

  const handleConvert = (e) => {
    e.preventDefault();
    axios.post(`http://localhost:8000/convert`, { code: code, language: lan },{  headers: {
      'Content-Type': 'application/json',
  
    }},)
      .then((res) => {
        setConv(res.data.result);
        console.log(res.data.result)
      })
      .catch((error) => {
        console.log(error);
      });
  };

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
      </form>

      <Box>
        {conv}
      </Box>
    </Box>
  );
};

export default Converter;
