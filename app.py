# Is an endpoint, no need to care about this
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask.globals import request
from chess_ai import getMoveMinimaxStr
from engine import get_engine_move
import chess
import json

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

@app.route('/naive', methods=['POST'])
def naive():
    req = request.get_json()
    fen = req["fen"]
    color = fen.split(" ")[1]
    if(color == "w"):
        color = "white"
    elif(color == "b"):
        color = "black"
    response = jsonify({'move' : getMoveMinimaxStr(fen, color)})
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    # response.headers.add('Access-Control-Allow-Origin', 'https://chess-webapp.com/')
    return response

@app.route('/engine', methods=['POST'])
def engine():
    req = request.get_json()
    res = {'move' : str(get_engine_move(req["fen"]))}
    response = jsonify(res)
    # response.headers.add('Access-Control-Allow-Origin', 'https://chess-webapp.com/')
    
    return response

@app.route('/testmove', methods=['GET','POST'])
def testmove():
    return jsonify({'move' : "d2d4"})
@app.route('/test', methods=['GET'])
def test():
    return "it does somewhat work"

