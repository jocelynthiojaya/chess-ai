from flask import Blueprint, render_template, session, redirect, url_for, request
from engine import get_engine_move
from chess_ai import getMoveMinimaxStr
bp = Blueprint("index", __name__, url_prefix="/")

@bp.route('/naive', methods = ['GET','POST'])
def naive():
    # req = request.get_json()
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    color = fen.split(" ")[1]
    if(color == "w"):
        color = "white"
    elif(color == "b"):
        color = "black"
    res = {'move' : str(getMoveMinimaxStr(fen, color))}
    return res

@bp.route('/engine', methods = ['GET','POST'])
def engine():
    # req = request.get_json()
    res = {'move' : str(get_engine_move("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"))}
    return res