

import { Box, Button, Select } from '@chakra-ui/react'
import React, { useState } from 'react'


const Converter = () => {
    const [code, setCode] = useState('');
    const [lan, setLang] = useState('');
    const [conv,setConv]=useState("")
    const handleConvert=()=>{
        

    }
  return (
    <>
    <Box m={4} w={10}> 

      <input type="text" placeholder='code' value={code} onChange={(e)=>setCode(e.target.value)}/>
      <Select onChange={(e)=>setLang(e.target.value)} placeholder={"langauge"} value={lan}>
        <option value="javascript">Javascript</option>
        <option value="java">Java</option>
        <option value="python">Python</option>
        <option value="c">C langauge</option>
      </Select>
      <Button onClick={handleConvert}>Convert</Button>

    </Box>


    </>
  )
}

export default Converter