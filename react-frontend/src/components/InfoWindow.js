import React, { useState, useEffect } from 'react'
import {Paper} from '@material-ui/core'
import { slotShouldForwardProp } from '@mui/material/styles/styled';

const InfoWindow = ({ cities, progress }) => {

    function rFact(num) {
        if (num === 0) { return 1; }
        else { return num * rFact(num - 1); }
    }

    function getCount(num) {
        if (num === 0) {
            return 0
        } else if (num === 1) {
            return 1
        } else if (num === 2) {
            return 1
        } else {
            return (rFact(num - 1)) / 2
        }
    }


    let solutionCount = getCount(cities.length)

    const isDone = useState(false)
    const [stats, setStats] = useState({})



    useEffect(()=>{

        setStats({
            ...stats,
            cityCount: cities.length,
            solutionCount: getCount(cities.length),
            solutionsChecked: progress > solutionCount ? solutionCount : progress,
            percentDone: (progress/solutionCount) > 1 ? "100.00" : (((progress / solutionCount) * 100).toFixed(2)),
        })
        
    }, [progress])



    return (
        <Paper className="info-window">
            <ul>
                <li>Number of cities:</li>
                <li>{stats.cityCount}</li>
                <li>Number of unique solutions:</li>
                <li>{stats.solutionCount}</li>
                <li>Solutions checked: {stats.solutionsChecked}</li>
                <li>Brute Force Progress: {stats.percentDone}%</li>
            </ul>
        </Paper>
    )
}

export default InfoWindow
