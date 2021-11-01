import React from 'react'
import {Circle} from 'react-konva'

const City = ({data, handleCityDrop, handleCityDrag}) => {
    return (
        <>
            <Circle
            key={data.key}
            name={data.key}
            // draggable
            // onDragEnd={handleCityDrop}
            onDragMove={handleCityDrag}
            x={data.x}
            y={data.y}
            fill={data.fill}
            radius={20}            
            />
        </>
    )
}

export default City
