import React from 'react'
import { Line } from 'react-konva'

const Road = ({data}) => {

    let points = [data.startx, data.starty, data.endx, data.endy]

    return (
        <Line
        points={points}
        stroke={'red'}

        
        />
    )
}

export default Road
