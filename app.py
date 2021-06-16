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
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    @app.route('/naive', methods=['POST'])
    def naive():
        req = request.get_json()
        fen = req["fen"]
        color = fen.split(" ")[1]
        if(color == "w"):
            color = "white"
        elif(color == "b"):
            color = "black"
        response = {}
        response['move'] = getMoveMinimaxStr(fen, color)
        return jsonify(response)

    @app.route('/engine', methods=['POST'])
    def engine():
        req = request.get_json()
        res = {'move' : str(get_engine_move(req["fen"]))}
        return jsonify(res)

    return app