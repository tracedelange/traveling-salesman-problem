import React from 'react'
import SubmissionMenu from './SubmissionMenu'


const Header = ({handleClearClick}) => {
    return (
        <div className="header">
            <SubmissionMenu />
            <h3>TSP - Interactive</h3>
            <button id='clear-cities' onClick={handleClearClick}>Clear Canvas</button>
        </div>
    )
}

export default Header
