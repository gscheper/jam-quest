import { Route, Routes } from 'react-router-dom';
import Home from './Routes/Home/Home';
import Queue from './Routes/Queue/Queue';
import Admin from './Routes/Admin/Admin';
import Quest from './Routes/Quest/Quest';

const Main = () => {
  return (
    <Routes> 
      <Route path='/' element={Home()}></Route>
      <Route path='/Queue' element={Queue()}></Route>
      <Route path='/Admin' element={Admin()}></Route>
      <Route path='/Quest' element={Quest()}></Route>
    </Routes>
  );
}

export default Main;