import React from 'react';
import { Route, Routes } from 'react-router-dom';
import ReactSwitch from 'react-switch';
import Home from './Routes/Home';
import Queue from './Routes/Queue';
import Admin from './Routes/Admin';

const Main = () => {
  return (
    <Routes> {/* The Switch decides which component to show based on the current URL.*/}
      <Route path='/' element={Home()}></Route>
      <Route path='/Queue' element={Queue()}></Route>
      <Route path='/Admin' element={Admin()}></Route>
    </Routes>
  );
}

export default Main;