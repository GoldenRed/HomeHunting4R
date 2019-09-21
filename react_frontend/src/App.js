import React, { useEffect, useState } from 'react';
import './App.css';
import Station from './Station';
import Place from './Place';

const App = ()=>{

  const station_num = 20;

  const [stations, setStations] = useState([]);
  const [address, setAddress] = useState([]);
  const [search, setSearch] = useState('');
  const [query, setQuery] = useState('');


  useEffect(()=> {
    getStations();
  }, [query])

  const getStations = async () => {
    const url = `http://hh4rapi-env.6gsmdkiciw.us-east-2.elasticbeanstalk.com/json/${query}/${station_num}` 
    const response = await fetch(url);
    //console.log(response);
    const data = await response.json();
    console.log(data);
    const stations_names = Object.keys(data)
    let stations_matrix = []
    let address_vec = []
    for (let i=0; i<stations_names.length; i++){
      if(stations_names[i] === 'QUERY_INFO'){
        address_vec.push(data[stations_names[i]][0]["query_lat"]);
        address_vec.push(data[stations_names[i]][0]["query_lng"]);
        //console.log(stations_names[i]);
        //console.log(data[stations_names[i]][0]["query_lat"], data[stations_names[i]][0]["query_lng"]);
      } else {
        stations_matrix.push([stations_names[i], data[stations_names[i]][0]["buss_fullLineID"][0], data[stations_names[i]][0]["distance"]]);
        //console.log(stations_names[i]);
        //console.log(data[stations_names[i]][0]["distance"]);
      }


    }
    setStations(stations_matrix);
    setAddress(address_vec);
  }

  const updateSearch = e => { 
    setSearch(e.target.value);
  }

  const getSearchQuery = e => {
    e.preventDefault();
    setQuery(search);
  }

  return (
    <div className="App">
      <form onSubmit={getSearchQuery} className="search-form">
        <label></label>
        <input className="search-bar" type="text" value={search} onChange={updateSearch}/>
          <button className = "search-button">
            Find closest UMD Stations
          </button>
      </form>
      <Place
        name={query}
        lat={address[0]}
        lng = {address[1]} 
      />
      <div className="stations">
        <ul>
      {stations.sort((a, b) => {return a[2]-b[2]}).map((station) => (
        <Station 
        title={station[0]}
        lineid={station[1]}
        distance={station[2]}
         />
      ))}
      </ul>
      </div>
    </div>
  );
};

export default App;
