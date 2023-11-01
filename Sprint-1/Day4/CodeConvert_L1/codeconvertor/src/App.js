import logo from './logo.svg';
import './App.css';
import CodeConveter from './Component/codeConveter';
import { Box } from '@chakra-ui/react';

function App() {
  return (
    <div className="App">
       <Box bgColor="#F5F5F5" minH="100vh">
      <CodeConveter/>
      </Box>
         </div>
  );
}

export default App;
