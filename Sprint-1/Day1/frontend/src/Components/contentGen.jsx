import { Box, Button, Heading, Input, Select, Spinner, Text } from '@chakra-ui/react'
import React, {  useState } from 'react'
import axios from "axios"
const Shayari = () => {
  const [type,setType]=useState("")
  const [keyword,setKeyword]=useState("")
  const [result, setResult] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  
  const demoData=[
    {
      "type": "shayari",
      "keywords": ["Love", "Heartbreak", "Friendship", "Life", "Nature","etc"]
    },
    {
      "type": "jokes",
      "keywords": ["Knock-knock", "Doctor", "School", "Animals", "Food","etc"]
    },
    {
      "type": "quotes",
      "keywords": ["Inspirational", "Motivational", "Success", "Happiness", "Friendship","etc"]
    },
    {
      "type": "stories",
      "keywords": ["Adventure", "Mystery", "Romance", "Fantasy", "Science Fiction","etc"]
    }
  ]
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    if(type==="" && keyword===""){
    alert("please selete type and keyword")

    }else{

   
    setIsLoading(true)
    try {
      const response = await axios.post(`https://content-generator1.onrender.com/get?type=${type}`, { keyword }, {
        headers: {
          'Content-Type': 'application/json',
        },
      })
      
      setResult(response.data.result);
      console.log("Type:", type);
      console.log("Keyword:", keyword);
      setKeyword("")
      setType("")
      
      console.log(response.data.result);
    } catch (error) {
      console.error(error);
      setIsLoading(false)
    } finally  {
      setIsLoading(false); // Set loading state to false after the API call is completed (success or error)
    };
  }
  };

  

return (
  <Box  bgColor={"pink.50"}minH="100vh" >
    <Heading > Content Generator</Heading>
    <Box p={4} maxW="md" mx="auto" >
      <Box  p={4} bgColor={"white"} boxShadow="rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px">
      <form onSubmit={handleSubmit} p={"25px"} >
        <Select value={type}   onChange={(e) => setType(e.target.value)} bgColor={"white"}>
          <option value="">Type</option>
          <option value="shayari">Shayari</option>
          <option value="jokes">Joke</option>
          <option value="quotes">Quote</option>
          <option value="stories">Story</option>
        </Select >
        <Input mt={"5px"} type="text" placeholder="Enter keyword" value={keyword} onChange={(e) => setKeyword(e.target.value)} bgColor={"white"}/>
        <Button type="submit" colorScheme="teal" mt={2}>
          Generate
        </Button>
      </form>
      <Box my={4} p={5}>
        {!isLoading ? <Text fontSize="md" color={"teal"}>{result}</Text> : <Spinner size="sm" color="teal.500" />}
      </Box>
      </Box>
      <Box p={5} bgColor={"gray.100"} boxShadow= "rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px">
        <Heading size="lg" mb={2}>
          Some Suggestions
        </Heading>
        {demoData.map((e, i) => (
          <Box key={i} mb={2} >
            <Heading size="md" mb={1}>
              Type: {e.type}
            </Heading>
            <Text fontSize="md">Keywords: {e.keywords.join(', ')}</Text>
          </Box>
        ))}
      </Box>
    </Box>
    </Box>
  );
};

export default Shayari