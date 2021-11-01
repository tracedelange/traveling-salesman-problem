import { useState, useEffect } from 'react'
import MainStage from './components/MainStage'
import Header from './components/Header'
import InfoWindow from './components/InfoWindow'
import { v4 as uuidv4 } from 'uuid';
import {shuffle} from './shuffle'
import { Route, Switch } from 'react-router-dom';
import AlgorithmSubmission from './components/AlgorithmSubmission';


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

function App() {

  const [lines, setLines] = useState([])
  const [cities, setCities] = useState([])

  const [randSol, setRandSol] = useState([])

  const [lastLine, setLastLine] = useState(null)

  const [progress, setProgress] = useState(-1)

  const handleClearClick = () => {

    setCities([])
    setRandSol([])
  }





  const tickSolution = () => {

    let newSol = [...cities]
    

    let newComb = newSol.sort( () => Math.random() - 0.5)
    newComb.push(newComb[0]) //Make sure the route loops back to the start

    setRandSol(newComb)
   

  }

  useEffect(() => {

    setProgress(progress + 1)

  }, [randSol])

  useEffect(() => {

    if (cities.length > 0){
      setProgress(0)
      const intervalID = setInterval(() => {
        tickSolution()
      }, 200);
    
      return function cleanup(){
        clearInterval(intervalID)
      }
    }
  }, [cities])


  // useEffect(() => {
  //   const intervalId = setInterval(() => {
  //     setLoadingStatus(ls => ls + ".");
  //   }, 1000);

  //   return () => clearInterval(intervalId);
  // }, []);

  const handleStageClick = (e) => {

    let r = Math.floor(Math.random() * 255);
    let g = Math.floor(Math.random() * 255);
    let b = Math.floor(Math.random() * 255);

    
    const newCity = {
      key: uuidv4(),
      name: uuidv4(),
      x: e.evt.offsetX,
      y: e.evt.offsetY,
      fill: `rgb(${r},${g},${b})`,
    }
    setCities(() => [...cities, newCity])


    let starting = cities[cities.length-1]

    // console.log(cities.length)

    if (cities.length !== 0) {

      let newLine = {
        key: uuidv4(),
        startName: starting.name,
        points: [starting.x, starting.y, e.evt.offsetX, e.evt.offsetY],
        stroke: 'red'
      } 

      if (cities.length >= 2) {

        let first = cities[0]

        let newLastLine = {
          key: uuidv4(),
          points: [first.x, first.y, e.evt.offsetX, e.evt.offsetY],
          stroke: 'red'
        }

        setLastLine(newLastLine)

      }

      setLines([...lines, newLine])
    } 


  }







  return (

    
    <div className="App">

      <Switch>
        <Route exact path='/solve'>

          <AlgorithmSubmission cities={cities} />

        </Route>
        <Route path='/'>
          <Header handleClearClick={handleClearClick}/>
          <InfoWindow progress={progress} cities={cities} />
          <MainStage
          handleStageClick={handleStageClick}
          cities={cities}
          lines={lines}

          randSolution={randSol}
          lastLine={lastLine}
          />
        </Route>

        </Switch>

    </div>
  );
}

export default App;
