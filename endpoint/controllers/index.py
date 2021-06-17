from flask import Blueprint, render_template, session, redirect, url_for, request
from endpoint.controllers.engine import get_engine_move
from endpoint.controllers.chess_ai import getMoveMinimaxStr
bp = Blueprint("index", __name__, url_prefix="/")

@bp.route('/naive', methods = ['GET','POST'])
def naive():
    req = request.get_json()
    fen = req["fen"]
    color = fen.split(" ")[1]
    if(color == "w"):
        color = "white"
    elif(color == "b"):
        color = "black"
    res = {'move' : str(getMoveMinimaxStr(fen, color))}
    return res

@bp.route('/engine', methods = ['GET','POST'])
def engine():
    req = request.get_json()
    fen = req["fen"]
    res = {'move' : str(get_engine_move(fen))}
    return res