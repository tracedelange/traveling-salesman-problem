import React, { useState, useEffect } from 'react';
import { render } from 'react-dom';
import { Stage, Layer, Rect, Text, Circle, Line } from 'react-konva';
import City from './City'
import { v4 as uuidv4 } from 'uuid';
import Road from './Road';
import { RGBA } from 'konva/lib/filters/RGBA';


const MainStage = ({ handleStageClick, cities, lines, lastLinem, randSolution }) => {

    // const [lines, setLines] = useState([])

    // const handleClick = (e) => {
    //     //call handle stage click and add a line
    //     handleStageClick(e)
    //     let starting = cities[cities.length-1]

    //     if (cities.length !== 0){
    //         console.log(starting)
    //         let newLine = {
    //             key: uuidv4(),
    //             points: [starting.x, starting.y, e.evt.offsetX, e.evt.offsetY],
    //             stroke: 'red'
    //         }

    //         setLines([...lines, newLine])
    //     }
    // }

    const handleCityDrop = (e) => {
        // e.target.attrs.x = e.evt.offsetX
        // e.target.attrs.y = e.evt.offsetY
    }

    const handleDrag = (e) => {
        // console.log(e.target.attrs)
        // // let line = lineArray.find((item) => item.props.data.startName === e.target.attrs.name)
        // // console.log(lineArray)
        // // console.log(line)
    }


    const cityArray = cities.map((item) => <City key={item.key} data={item} handleCityDrag={handleDrag} handleCityDrop={handleCityDrop} />)
    // const lineArray = lines.map((item) => <Road key={item.key} data={item} />)

    // const solLineArray = randSolution.map((item) => <Road key={item.key} data={item}/>)
    let solLineArray = []
    for (let i = 0; i < randSolution.length - 1; i++){
        let data = {
            startx: randSolution[i].x,
            starty: randSolution[i].y,
            endx: randSolution[i+1].x,
            endy: randSolution[i+1].y,
        }

        solLineArray.push(<Road key={randSolution[i].key} data={data} />)
    }

    // console.log(cityArray.length > 0 ? 'true' : 'false')

    

    return (
        <Stage width={window.innerWidth} height={(window.innerHeight) - ((window.innerHeight) * .05)} background={'black'} onClick={handleStageClick}>
            <Layer>
                <Rect
                width={window.innerWidth}
                height={(window.innerHeight) - ((window.innerHeight) * .05)}
                x={0}
                y={0}
                fill={"#012A36"}
                
                />
            </Layer>
            <Layer>
                {solLineArray}
                {/* {lineArray} */}
                {/* {lastLine ? <Road key={lastLine.key} data={lastLine } /> : null} */}
            </Layer>
            <Layer>
                {cityArray}
            </Layer>
        </Stage>
    );
}

export default MainStage
