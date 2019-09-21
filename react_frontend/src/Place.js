import React from 'react';

const Place = ({name, lat, lng}) =>{
    if(name === ''){
        return (
            <div>
                <h3> Make a search!</h3>
            </div>
        )
    }
    else{
    return (
    <div>
        <h3>Your Place: {name}</h3>
        <p> Latitude: {lat} <br></br> Longtitude: {lng}</p>
    </div>
    );
};
}

export default Place;