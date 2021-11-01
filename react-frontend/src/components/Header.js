import React from 'react'
import SubmissionMenu from './SubmissionMenu'
import { Button } from '@material-ui/core'

const Header = ({handleClearClick}) => {
    return (
        <div className="header">
            {/* <SubmissionMenu /> */}
            <div className='first'>
            </div>
            <div className='second'>
                <h3>Travelling Salesman Problem</h3>
            </div>
            <div className='third'>
                <Button id='clear-cities' sx={{backgroundColor: 'red'}} variant='outlined' onClick={handleClearClick}>Clear Canvas</Button>
            </div>
            {/* <button id='clear-cities' onClick={handleClearClick}>Clear Canvas</button> */}
        </div>
    )
}

export default Header
