import React, { useState } from 'react'

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

    return (
        <div className="info-window">
            <ul>
                <li>Number of cities:</li>
                <li>{cities.length}</li>
                <li>Number of unique solutions:</li>
                <li>{solutionCount}</li>
                <li>Solutions checked: {progress > solutionCount ? solutionCount : progress}</li>
                <li>Brute Force Progress: { (progress/solutionCount) > 1 ? "100.00" : (((progress / solutionCount) * 100).toFixed(2)) }%</li>
            </ul>
        </div>
    )
}

export default InfoWindow
