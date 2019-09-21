import React from 'react';
import style from './station.module.css';

const Station = ({title,lineid, distance}) =>{
    return (
    <li className={style.listItem}>
        <div className={style.station}>
            <h3>{title}</h3>
            <h4>Line: {lineid}</h4>
            <h4>{distance.toFixed(2)} km away.</h4>
        </div>
    </li>
    );
}

export default Station;