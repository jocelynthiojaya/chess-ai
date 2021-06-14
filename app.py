# Is an endpoint, no need to care about this
from flask import Flask
from flask.globals import request
from chess_ai import getMoveMinimax
from engine import get_engine_move

app = Flask(__name__)

@app.route('/naive', methods=['POST'])
def naive():
    req = request.get_json()
    color = req.fen.split(" ")[1]
    return getMoveMinimax(req.fen, color)

@app.route('/engine', methods=['POST'])
def engine():
    req = request.get_json()
    return get_engine_move(req.fen)