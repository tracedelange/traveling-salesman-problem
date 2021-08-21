import React from 'react'

const Header = ({handleClearClick}) => {
    return (
        <div className="header">
            <h3>TSP - Interactive</h3>
            <button id='clear-cities' onClick={handleClearClick}>Clear Canvas</button>
        </div>
    )
}

export default Header
