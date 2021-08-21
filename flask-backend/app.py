import flask
from flask import request, jsonify, Flask
from os import environ
import random

app = flask.Flask(__name__)



@app.route('/', methods=['GET'])
def home():
	return """
    <h1>TSP API</h1>
    <h2>The purpose of this API is to calculate solutions to the travelling salesman problem
    using both brute force methods and evolutionary genetic algorithms</h2>
    <h2>If you'd like to visit the front-end site that cooresponds with this project, you can visit it <a href="https://github.com/tracedelange/traveling-salesman-problem/tree/overhaul/react-frontend" >here</a><h2/>
    
    <br/>

    <h2>Developed By <a href="https://www.delangedev.com/">Trace DeLange</a></h2>



    <h3>Routes:</h3>
    <ul>
        <li style="font-size: 3vmin;">
            /brute-force
        </li>
    
    </ul>
    
    """
@app.route('/test', methods=['GET'])
def test():
    return jsonify(random.randint(0,1000000))

if __name__ == "__main__":
    app.run(debug=True)