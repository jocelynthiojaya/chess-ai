# Is an endpoint, no need to care about this
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask.globals import request
from chess_ai import getMoveMinimaxStr
from engine import get_engine_move
import chess
import json

def get_app():
    app = Flask(__name__)
    app.config['CORS_HEADERS'] = 'Content-Type'
    cors = CORS(app)

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
        print(response)
        # response.headers.add('Access-Control-Allow-Origin', 'https://chess-webapp.com/')
        return jsonify(response)

    @app.route('/engine', methods=['POST'])
    def engine():
        req = request.get_json()
        res = {'move' : str(get_engine_move(req["fen"]))}
        response = jsonify(res)
        response.headers.add('Access-Control-Allow-Origin', 'https://chess-webapp.com/')
        
        return res

    return app