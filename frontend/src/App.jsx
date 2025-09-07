import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import {BrowserRouter, Route, Routes} from 'react-router-dom'
import Home from './components/Home'
import HooksLearn from './pages/HooksLearn'

function App() {
  const [count, setCount] = useState(0)

  return (
   <BrowserRouter>
    <Routes>
      <Route path='/count' element={<HooksLearn />} />
      <Route path='*' element={<Home />}/>
      
    </Routes>
   </BrowserRouter>
  )
}

export default App
