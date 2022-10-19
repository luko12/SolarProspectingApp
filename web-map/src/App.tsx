import React from 'react';
import logo from './logo.svg';
import './App.css';



function App() {

  const mapboxgl = require('mapbox-gl/dist/mapbox-gl.js');
  mapboxgl.accessToken = process.env.REACT_APP_MAPBOX_TOKEN;
  // var map = new mapboxgl.Map({
  //   container: 'YOUR_CONTAINER_ELEMENT_ID',
  //   style: 'mapbox://styles/mapbox/streets-v11'
  // });

  return (
    <div className="App">
      <div>lukas' web map</div>
      
    </div>
  );
}

export default App;
